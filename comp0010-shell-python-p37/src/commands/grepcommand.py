"""
Imports the base commmand, and implements the interface for the grep command
"""
import re
from io import StringIO, TextIOWrapper
from typing import List

from commands.base_command import BaseCommand
from commands.command_helpers import exception_handled_open, is_stream_empty
from commands.command_spec import CommandSpecification
from errors.command_errors import CommandError
from flag import FlagValue


class Grep(BaseCommand):
    """
    class for the grep command, which implements the BaseCommand interface
    """

    COMMAND_SPECIFICATION = \
        CommandSpecification("grep", [],
                             (
                                 "PATTERN [FILE]...",
                                 "Searches [FILE]... for lines containing a"
                                 " match to PATTERN\n"
                                 "  PATTERN is a regular expression in PCRE "
                                 "format.\n"
                                 "  FILE is the name of a file.",
                             ))

    def __init__(
        self,
        in_stream: StringIO,
        out_stream: StringIO,
        flags: List[FlagValue],
        options: List[str],
    ) -> None:
        """
        Initializes the CD object with input and output streams.

        Args:
            in_stream (StringIO): Input stream for the command.
            out_stream (StringIO): Output stream for the command.
            flags (List[FlagValue]): List of flags supported by the command.
            options (List[str]): List of options supported by the command.
        """
        try:
            self.pattern = re.compile(options[0])
        except re.error as e:
            raise CommandError("Invalid pattern: " + options[0]) from e

        super().__init__(in_stream, out_stream, flags, options)

    def _grep(self, file: TextIOWrapper) -> List[str]:
        """
        Helper function to grep a file

        Args:
            file (TextIOWrapper): The file to grep

        Returns:
            List[str]: The lines that match the pattern
        """
        lines = []
        for line in file:
            if self.pattern.search(line):
                lines.append(line)
        return lines

    def run(self) -> int:
        """
        see BaseCommand.run()

        Returns:
            int: exit code of the function

        Raises:
            CommandError: if an OSError or PermissionError is thrown
            ShellFileNotFoundError: if the given file cannot be found
        """

        if len(self.options) < 2:
            if is_stream_empty(self.input):
                raise CommandError("No input provided")
            self.output.writelines(self._grep(self.input))
            return 0
        files = self.options[1:]
        for file in files:
            with exception_handled_open(file, "r") as f:
                for line in self._grep(f):
                    if len(files) > 1:
                        self.output.write(f"{file}:{line}")
                    else:
                        self.output.write(line)

        return 0
