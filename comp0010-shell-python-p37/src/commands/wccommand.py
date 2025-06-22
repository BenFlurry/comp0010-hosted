"""
Module for the we command.
"""
from io import StringIO, TextIOWrapper
from typing import List

from commands.base_command import (BaseCommand, CommandSpecification,
                                   FlagSpecification)
from commands.command_helpers import exception_handled_open, is_stream_empty
from errors.command_errors import CommandError
from flag import FlagValue


class WC(BaseCommand):
    """
    class for the wc command, which implements the BaseCommand interface
    """
    COMMAND_SPECIFICATION = CommandSpecification("wc", [
        FlagSpecification('l', bool, 'Print the newline counts'),
        FlagSpecification('w', bool, 'Print the word counts'),
        FlagSpecification('m', bool, 'Print the byte counts')
    ], (
        "[OPTIONS] [FILE]",
        "Prints the newline, word, and byte counts for FILE.\n"))

    def __init__(self, in_stream: StringIO, out_stream: StringIO,
                 flags: List[FlagValue], options: List[str]) -> None:
        """
        Initializes the CD object with input and output streams.

        Args:
            in_stream (StringIO): Input stream for the command.
            out_stream (StringIO): Output stream for the command.
            flags (List[FlagValue]): List of flags supported by the command.
            options (List[str]): List of options supported by the command.
        """
        self.check_flags(flags)
        super().__init__(in_stream, out_stream, flags, options)

    def check_flags(self, flags) -> None:
        """
        Checks if the flags are valid.

        Args:
            flags (List[FlagValue]): List of flags supported by the command.

        Raises:
            CommandError: if the flags are not valid
        """
        if len(flags) > 1:
            raise CommandError("Invalid number of flags")
        if flags and flags[0].name not in ['l', 'w', 'm']:
            raise CommandError("Invalid Flag Name")

    def _count_all(self, in_stream: TextIOWrapper) -> List[int]:
        """
        Counts the number of lines, words, and chars in the input stream.

        Args:
            in_stream (TextIOWrapper): Input stream for the command.

        Returns:
            List[int]: A list of the number of lines, words, then chars
        """
        num_lines = 0
        num_words = 0
        num_chars = 0

        for line in in_stream:
            num_lines += 1
            num_words += len(line.split())
            num_chars += len(line)
        return [num_lines, num_words, num_chars]

    def _wc(self, in_stream: StringIO) -> None:
        """
        Prints the wc of the input stream.

        Args:
            in_stream (StringIO): Input stream for the command.
        """
        counts = self._count_all(in_stream)

        if not self.flags:
            self.output.write(f"{counts[0]} {counts[1]} {counts[2]}")
            return

        for flag in self.flags:
            if flag.name == 'l':
                self.output.write(f"{counts[0]}")
            elif flag.name == 'w':
                self.output.write(f"{counts[1]}")
            else:
                self.output.write(f"{counts[2]}")

    def run(self) -> int:
        """
        Runs the wc command.
        """
        if len(self.options) == 0:
            if is_stream_empty(self.input):
                raise CommandError()
            self._wc(self.input)
            return 0

        combined_file = StringIO()
        for file in self.options:
            with exception_handled_open(file, 'r') as f:
                combined_file.write(f.read())
        combined_file.seek(0)
        self._wc(combined_file)
        self.output.write("\n")
        return 0
