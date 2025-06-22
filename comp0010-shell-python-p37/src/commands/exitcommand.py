"""
This module contains the ExitCommand class.
"""
from commands.base_command import BaseCommand
from commands.command_spec import CommandSpecification
from flag import WildcardFlagSpecification
from errors.shell_errors import ShellExitError


class Exit(BaseCommand):
    """
    A class representing the exit command.
    """

    COMMAND_SPECIFICATION = CommandSpecification(
        "exit", [WildcardFlagSpecification()], ("", "Exits the shell")
    )

    def run(self) -> int:
        """
        see BaseCommand.run()
        """
        raise ShellExitError()
