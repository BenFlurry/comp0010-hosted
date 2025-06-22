"""
Module for the sort command.
"""
import os
from io import StringIO
from typing import List

from errors.command_errors import CommandError, ShellFileNotFoundError
from errors.error_dsi import DeveloperSkillIssue
from flag import FlagValue, FlagSpecification
from commands.command_spec import CommandSpecification
from commands.base_command import BaseCommand


class Sort(BaseCommand):
    """
    class for the sort command, which implements the BaseCommand interface
    """

    COMMAND_SPECIFICATION = CommandSpecification(
        "sort",
        [FlagSpecification("r", bool, "reverse sort")],
        (
            "[-r] [FILE]",
            "Sorts the lines in a file\n"
            "  [-r] sorts lines in reverse order\n"
            "  [FILE] is the file to sort",
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
        """
        self._check_flags_guard(flags, options)
        super().__init__(in_stream, out_stream, flags, options)

    def _check_flags_guard(
        self, flags: List[FlagValue], options: List[str]
    ) -> None:
        if len(flags) > 1:
            raise CommandError("sort only accepts one flag")
        if flags and flags[0].name != "r":
            raise DeveloperSkillIssue(
                "sort only accepts the -r flag. This "
                "should have been caught by the parser"
            )
        if len(options) > 1:
            raise CommandError("sort only accepts one file")

    def _file_helper(self, file_name: str) -> List[str]:
        """
        Sorts the lines in a file and writes them to the output stream.
        Args:
            file_name (str): Name of the file to sort.
        """
        try:
            with open(file_name, "r") as file:
                lines = file.readlines()
        except PermissionError as e:
            raise CommandError(
                "process does not have permission to open the file"
            ) from e
        except OSError as e:
            raise CommandError("error reading file") from e

        return lines

    def run(self) -> int:
        """
        see BaseCommand.run()
        """
        if len(self.options) == 0:
            self.input.seek(0, os.SEEK_END)
            if self.input.tell() == 0:
                raise CommandError("sort needs a file or stdin")
            self.input.seek(0)
        else:
            if not os.path.exists(self.options[0]):
                raise ShellFileNotFoundError(self.options[0])
        if self.options:
            lines = self._file_helper(self.options[0])
        else:
            lines = self.input.readlines()

        lines.sort(reverse=("r" in [flag.name for flag in self.flags]))
        for line in lines:
            self.output.write(line)

        return 0
