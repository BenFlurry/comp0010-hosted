"""
module for the cat command, which implements the BaseCommand interface
"""
from io import StringIO
from typing import List

from commands.base_command import BaseCommand
from commands.command_helpers import exception_handled_open, is_stream_empty
from commands.command_spec import CommandSpecification
from errors.command_errors import CommandError, UnknownFlagError
from flag import FlagValue


class CAT(BaseCommand):
    """
    class for the cat command, which implements the BaseCommand interface
    """

    COMMAND_SPECIFICATION = CommandSpecification(
        "cat", [], ("[FILE]...", "Concatenate FILE(s) to standard output.")
    )

    def __init__(
        self,
        in_stream: StringIO,
        out_stream: StringIO,
        flags: List[FlagValue],
        options: List[str],
    ) -> None:
        """
        Initializes the CAT object with input and output streams.

        Args:
            in_stream (StringIO): Input stream for the command.
            out_stream (StringIO): Output stream for the command.
            flags (List[FlagValue]): List of flags supported by the command.
            options (List[str]): List of options supported by the command.
        """
        super().__init__(in_stream, out_stream, flags, options)
        if self.flags:
            raise UnknownFlagError

    def run(self) -> int:
        """
        see BaseCommand.run()
        Raises:
            ShellFileNotFoundError: if the file option does not exist
            CommandError: if invalid or no options are provided
        """
        if not is_stream_empty(self.input):
            self.output.write(self.input.read())
            return 0

        if not self.options:
            raise CommandError("cat requires a file passed as an option")

        for option in self.options:
            with exception_handled_open(option, 'r') as file:
                self.output.write(file.read())

            self.output.write("")
        return 0
