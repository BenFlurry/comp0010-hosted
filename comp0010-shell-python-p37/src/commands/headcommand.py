"""
Imports the base commmand, and implements the interface for the head command
"""
from typing import List
from io import StringIO, TextIOWrapper

from flag import FlagValue, FlagSpecification, Flag
from errors.command_errors import CommandError
from errors.error_dsi import DeveloperSkillIssue
from commands.base_command import BaseCommand
from commands.command_spec import CommandSpecification
from commands.command_helpers import exception_handled_open, is_stream_empty


class Head(BaseCommand):
    """
    class for the head command, which implements the BaseCommand interface
    """

    COMMAND_SPECIFICATION = CommandSpecification(
        "head",
        [FlagSpecification("n", int, "Number of lines to print")],
        (
            "[OPTIONS] [FILE]",
            "Prints the first 10 lines of FILE if -n is not provided.\n",
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
        Initializes the CD object with input and output streams. Also checks
        for flag validity.

        Args:
            in_stream (StringIO): Input stream for the command.
            out_stream (StringIO): Output stream for the command.
            flags (List[FlagValue]): List of flags supported by the command.
            options (List[str]): List of options supported by the command.

        Raises:
            DeveloperSkillIssue: if the number of lines is not valid
        """
        self.num_lines: int = self._check_num_lines(flags)
        super().__init__(in_stream, out_stream, flags, options)

    def _check_num_lines(self, flags: List[Flag]) -> int:
        """
        Checks if the number of lines to be read is valid,

        Args:
            flags (List[Flag]): the number of lines to be read from the file
        Raises:
            DeveloperSkillIssue: if the number of lines is not valid
        """
        num_lines: int = 10
        for flag in flags:
            if flag.name == "n":
                if not isinstance(flag.value, int):
                    raise DeveloperSkillIssue(
                        f"Invalid number of lines \
                                                {flag.value}, should have \
                                                been caught by flag \
                                                parser"
                    )
                num_lines = int(flag.value)
            else:
                raise DeveloperSkillIssue(
                    f"Invalid flag {flag.name}, should \
                                            have been caught by flag parser"
                )
        return num_lines

    def _read_lines_from_file(
        self, f: TextIOWrapper, num_lines: int
    ) -> List[str]:
        """
        Reads up to num_lines from the specified file.

        Args:
            file (TextIOWrapper): file object
            num_lines (int): Maximum number of lines to read.

        Returns:
            List[str]: List of lines read from the file.

        Raises:
            FileNotFoundError: If the file is not found.
        """
        lines: List[str] = f.readlines()
        # Count from the end if num_lines is negative
        if num_lines < 0:
            num_lines = len(lines) + num_lines
        # Keep num_lines within the range [0, file_len]
        num_lines = min(max(num_lines, 0), len(lines))
        return lines[:num_lines]

    def run(self) -> int:
        """
        see BaseCommand.run()

        Raises:
            ShellFileNotFoundError: if the file cannot be found
            CommandError: if the opening of the file raises an OSError, or if
                unauthorised
        Returns:
            int: exit code of the function (0 if successful)
        """
        if len(self.options) != 1 and is_stream_empty(self.input):
            raise CommandError()

        lines_to_output: List[str]

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
