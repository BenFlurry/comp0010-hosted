"""
Code related to flags
"""
from dataclasses import dataclass
from typing import Generic, List, Type, TypeVar, Union, get_args, get_origin

from errors.error_dsi import DeveloperSkillIssue, check_arguments
from errors.parse_errors import UnknownFlagValueError

T = TypeVar('T', bool, str, int, float, List[str], List[int], List[float])


@dataclass
class Flag(Generic[T]):
    """
    A data class that represents the flag, its value, and its help text
    """
    name: str
    value: T
    help_text: str


@dataclass
class FlagSpecification(Generic[T]):
    """
    A specification class that embeds the typing information of the value. To
    construct a flag from a flag specification, use the build_flag() function.
    """
    name: str
    value_type: Type[T]
    help_text: str

    @check_arguments
    def build_flag_from_string(self, value: str) -> Flag[T]:
        """
        Builds a flag from a string value.

        Assumptions (non-standard Pydoc):
            For the sake of performance, I'm assuming lists are homogeneous

        Arguments:
            value (str): A raw string to be parsed into Flags

        Returns:
            Flag: A complete flag object

        Throws:
            UnknownFlagValueError: If a builder function fails to build a flag,
                                   this exception is thrown
        """
        # value_type usually contains a type, which can construct values
        # out of strings.

        # Atomically, we're dealing with int, float and strs, and all three
        # do indeed qualify as proper builder functions.

        # For lists, we simply acquire the atomic types and build over the
        # array
        try:
            if get_origin(self.value_type) == list:
                builder_fn = get_args(self.value_type)[0]
                return self.build_flag_with_value(
                    [
                        builder_fn(val.strip())
                        for val in value.split(',')
                    ])
            builder_fn = self.value_type
            return self.build_flag_with_value(builder_fn(value))
        except ValueError as e:
            raise UnknownFlagValueError(
                f"Invalid value for flag {self.name}: {value}"
            ) from e

    @check_arguments
    def build_flag_with_value(self, value: T) -> Flag[T]:
        """
        Builds a flag with the value being of type T, the type of this
        specification.

        Arguments:
            value (T): The value to build the flag with.

        Returns:
            Flag: A complete flag object
        """
        if get_origin(self.value_type) != list and \
           not isinstance(value, self.value_type):
            raise DeveloperSkillIssue('Flag value was not the correct type. '
                                      'Something wrong with the parsing '
                                      'integration?')
        return Flag(self.name, value, self.help_text)


FlagValue = Union[
    Flag[bool],
    Flag[str],
    Flag[int],
    Flag[float],
    Flag[List[str]],
    Flag[List[int]],
    Flag[List[float]]
]
