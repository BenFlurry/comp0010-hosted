"""
A wildcard flag specification. This is useful for commands like echo; echo
accepts all input even if they are not valid flags.
"""

from typing import TypeVar

from errors.error_dsi import DeveloperSkillIssue

from .flag import Flag, FlagSpecification

WILDT = TypeVar('WILDT', bool, str)


class WildcardFlagSpecification(FlagSpecification[bool]):
    """
    The wildcard flag specification. All parsers that encounter this
    specification must add the "flag" as an option rather than a flag.

    WildcardFlagSpecification inherits from FlagSpecification as a "boolean"
    flag, for proper inheritance - however, all functions declared within
    FlagSpecification will raise an exception, as this specification is not
    meant to build a flag.

    Class specificaitons from the WildcardFlagSpecification should be
    completely ignored.
    """

    def __init__(self):
        super().__init__('', bool, '')

    @property
    def name(self) -> str:  # type: ignore[return]
        """
        Getting the name property will result in a DSI, because it is not meant
        to be used as a flag
        """
        self.raise_dsi()

    @name.setter
    def name(self, _: str) -> None:
        # all setters will silently drop values. This is required, otherwise
        # mypy will complain we're trying to make a writable attribute in the
        # base class and calling the base constructor will cause a
        # DeveloperSkillIssue
        pass

    @property
    def value_type(self) -> type:  # type: ignore[return]
        """
        Getting the value type property will result in a DSI, because it is not
        meant to be used as a flag
        """
        self.raise_dsi()

    @value_type.setter
    def value_type(self, _: str) -> None:
        pass

    @property
    def help_text(self) -> str:  # type: ignore[return]
        """
        Getting the help text property will result in a DSI, because it is not
        meant to be used as a flag
        """
        self.raise_dsi()

    @help_text.setter
    def help_text(self, _: str) -> None:
        pass

    def raise_dsi(self) -> None:
        """This property always throws the DeveloperSkillIssue exception"""
        raise DeveloperSkillIssue(
            'None of the attributes of the wildcard flag specification should'
            ' be accessed.'
        )

    def build_flag_with_value(self, value: bool) -> Flag[bool]:
        """It should not be possible to build a wildcard flag"""
        raise DeveloperSkillIssue(
            'WildCardFlagSpecification is not meant to be used to build'
            ' a flag. Implementers should pass this parameter as an option'
            ' instead.')
