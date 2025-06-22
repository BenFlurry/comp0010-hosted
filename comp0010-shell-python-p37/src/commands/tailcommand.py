"""
Imports the base commmand, and implements the interface for the tail command
"""
from io import StringIO, TextIOBase
from typing import List

from commands.base_command import BaseCommand
from commands.command_helpers import exception_handled_open, is_stream_empty
from commands.command_spec import CommandSpecification
from errors.command_errors import CommandError
from errors.error_dsi import DeveloperSkillIssue
from flag import Flag, FlagSpecification, FlagValue


class Tail(BaseCommand):
    """
    class for the tail command, which implements the BaseCommand interface
    """

    COMMAND_SPECIFICATION = CommandSpecification(
        "tail",
        [FlagSpecification("n", int, "Number of lines to print")],
        (
            "[OPTIONS] [FILE]",
            "Prints the last 10 lines of FILE if -n is not provided.\n",
        ),
    )

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

        Raises:
            DeveloperSkillIssue: if the number of lines is not valid
            CommandError: if the number of options is not 1
        """
        self.num_lines = self._check_num_lines(flags)
        super().__init__(in_stream, out_stream, flags, options)

    def _check_num_lines(self, flags: List[Flag]) -> int:
        """
        Checks if the number of lines to be read is valid, and returns the
        number of lines to be read if it is valid. Returns 10 if the number
        of lines is not specified.

        Args:
            lines (int): the number of lines to be read from the file
        Raises:
            UnknownFlagValueError: if the number of lines is not valid
        """
        # set the default number of lines to be read to 10
        num_lines: int = 10
        for flag in flags:
            if flag.name == "n":
                if not isinstance(flag.value, int):
                    raise DeveloperSkillIssue(
                        f"Invalid number of lines \
                                                {flag.value}"
                    )
                num_lines = flag.value
                break
            raise DeveloperSkillIssue(
                f"Invalid flag {flag.name}, should have \
                                      been caught by flag parser"
            )
        return num_lines

    def _read_lines_from_file(
        self, f: TextIOBase, num_lines: int
    ) -> List[str]:
        """
        Reads up to num_lines from the specified file.

        Args:
            f (TextIOBase): A file stream
            num_lines (int): Maximum number of lines to read.

        Returns:
            List[str]: List of lines read from the file.

        Raises:
            FileNotFoundError: If the file is not found.
        """
        lines = f.readlines()
        # If the number of lines is negative, read the last abs(num_lines)
        if num_lines < 0:
            num_lines = abs(num_lines)
        # Don't read more lines than there are in the file
        num_lines = min(num_lines, len(lines))

        return lines[len(lines) - num_lines:]

    def run(self) -> int:
        """
        see BaseCommand.run()

        Raises:
            ShellFileNotFoundError
        """
        if len(self.options) != 1 and is_stream_empty(self.input):
            raise CommandError("No file specified")

        if self.options:
            file = self.options[0]
            with exception_handled_open(file, "r") as f:
                lines_to_output = self._read_lines_from_file(f, self.num_lines)
        else:
            lines_to_output = self._read_lines_from_file(
                self.input, self.num_lines
            )

        for line in lines_to_output:
            self.output.write(line)

        return 0
