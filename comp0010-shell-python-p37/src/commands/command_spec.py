"""
A command specification class.

This class is built to be called by the parser before the instantiation of
Command. The idea is to mimic the restriction of normal OOP languages where
abstract classes can't have abstract properties.
"""

from dataclasses import dataclass
from typing import List, Tuple

from errors.error_dsi import DeveloperSkillIssue
from flag import FlagSpecification

HELP_FLAG = FlagSpecification("h", bool, "Displays this help text")


@dataclass
class CommandSpecification:
    """
    CommandSpecification is a dataclass that contains the flag specifications
    """
    _command_name: str
    _flag_specifications: List[FlagSpecification]
    _command_help_text: Tuple[str, str]

    @property
    def command_name(self) -> str:
        """
        The command name of this command
        Returns:
            str: the command name
        """
        return self._command_name

    @property
    def flag_specifications(self) -> List[FlagSpecification]:
        """
        The list of flags that this command accepts.
        Returns:
            List[Flag]: Flags support by this command
        """
        return self._flag_specifications + [HELP_FLAG]

    @property
    def command_help_text(self) -> Tuple[str, str]:
        """
        The list of flags that this command accepts.
        Returns:
            List[Tuple[str, str]]: Flags support by this command
        """
        return self._command_help_text


class AbstractCommandSpecification(CommandSpecification):
    """
    AbstractCommandSpecification will throw an error for all defined attributes
    """

    def __init__(self):
        super().__init__('', [], ('', ''))

    @property
    def command_name(self) -> str:
        """
        The property command name. Because this is abstract, this will throw an
        error
        """
        raise DeveloperSkillIssue(
            "a specification should have been written for this cmd")

    @property
    def flag_specifications(self) -> List[FlagSpecification]:
        """
        The flag specification. Because this is abstract, this will throw an
        error
        """
        raise DeveloperSkillIssue(
            "a specification should have been written for this cmd")

    @property
    def command_help_text(self) -> Tuple[str, str]:
        """
        Command help text. Because this is abstract, this will throw an error
        """
        raise DeveloperSkillIssue(
            "a specification should have been written for this cmd")
