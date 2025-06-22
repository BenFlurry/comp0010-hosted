"""
This module contains the UniqCommand class.
"""
from io import StringIO, TextIOWrapper
from typing import List
import os

from errors.command_errors import CommandError, ShellFileNotFoundError
from errors.error_dsi import DeveloperSkillIssue
from flag import FlagValue, FlagSpecification

from commands.base_command import BaseCommand
from commands.command_spec import CommandSpecification
from commands.command_helpers import exception_handled_open


class Uniq(BaseCommand):
    """
    Class for the uniq command, which implements the BaseCommand interface
    """

    COMMAND_SPECIFICATION = CommandSpecification(
        "uniq",
        [FlagSpecification("i", bool, "ignore case")],
        (
            "[-i] [FILE]...",
            "Prints the unique lines in [FILE]...\n"
            "  -i: ignore case when doing the comparison\n"
            "  FILE is the name of a file.",
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
            raise CommandError("uniq only accepts one flag")
        if flags and flags[0].name != "i":
            raise DeveloperSkillIssue(
                "uniq only accepts the -i flag. This "
                "should have been caught by the parser"
            )

        if len(options) > 1:
            raise CommandError("uniq only accepts one file")

    def _uniq(self, file: TextIOWrapper) -> None:
        """
        Core uniq functionality
        """
        prev_line = ""
        for line in map(lambda x: x.strip(), file):
            if "i" in [x.name for x in self.flags]:
                if line.lower() != prev_line.lower():
                    self.output.write(line + "\n")
            else:
                if line != prev_line:
                    self.output.write(line + "\n")
            prev_line = line

    def run(self) -> int:
        """
        see BaseCommand.run()
        """
        if len(self.options) == 0:
            # check if stdin is empty, if so, raise an error
            self.input.seek(0, os.SEEK_END)
            if self.input.tell() == 0:
                raise CommandError("uniq needs a file or stdin")
            self.input.seek(0)
            self._uniq(self.input)
            return 0

        if not os.path.exists(self.options[0]):
            raise ShellFileNotFoundError(self.options[0])

        with exception_handled_open(self.options[0], "r") as file:
            self._uniq(file)

        return 0
