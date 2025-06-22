"""
Imports BaseCommand interface and implements it with the find command
"""

import os
import fnmatch
from io import StringIO
from typing import List

from errors.command_errors import (
    CommandError,
    ShellFileNotFoundError,
    UnknownFlagError,
    UnknownFlagValueError,
)
from errors.error_dsi import DeveloperSkillIssue
from flag import FlagValue, FlagSpecification
from commands.base_command import BaseCommand
from commands.command_spec import CommandSpecification


class Find(BaseCommand):
    """
    class for the find command, which implements the BaseCommmand interface
    """

    COMMAND_SPECIFICATION = CommandSpecification(
        "find",
        [FlagSpecification("name", str, "search expression")],
        (
            "EXPR, PATH",
            "Searches for the given EXPR in for files under PATH\n",
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
        Initializes the Find object with in_stream and out_stream streams.

        Args:
            in_stream (StringIO): Input stream for the command.
            out_stream (StringIO): Output stream for the command.
            flags (List[FlagValue]): List of flags supported by the command.
            options (List[str]): List of options supported by the command.
        """

        self.path = ""
        self.search_expr = ""
        self._check_flags_and_options(flags, options)
        self.found_items: List[str] = []
        super().__init__(in_stream, out_stream, flags, options)

    def _check_flags_and_options(self, flags, options) -> None:
        """
        Checks that if no options are supplied, then path is set to cwd
        If an option is supplied, checks that the path supplied is valid
        If more than 1 option is supplied, throws a command error

        Arguments:
            options (List[str]): the list of options passed into the init func

        Raises:
            ShellFileNotFoundError: if the given path cannot be found
            CommandError: if too many options are given
            DeveloperSkillIssue: if a flag is provided that isn't called name
        """
        # check the options are valid
        if len(options) == 0:
            self.path = "."

        elif len(options) == 1:
            path = options[0]
            if not os.path.exists(path):
                raise ShellFileNotFoundError()
            self.path = path

        else:
            raise CommandError("Too many options supplied")

        # check the flags are valid
        if len(flags) > 1:
            raise UnknownFlagError("Command requires 1 flag")

        if len(flags) == 0:
            self.search_expr = "*"
            return

        flag = flags[0]
        if flag.name != "name":
            raise DeveloperSkillIssue

        if not isinstance(flag.value, str):
            raise UnknownFlagValueError("Flag value has to be a string")

        self.search_expr = flag.value

    def find(self, path) -> None:
        """
        A helper function which recurses through a file structure, returning
        the path to files which match the search expression stated by the flag

        Arguments:
            path (str): the current path in the recursive traversal of the file
                structure

        Raises:
            ShellFileNotFoundError: when the specified path option cannot be
                found
            CommandError: if permission is denied, or the path specified was
                not a directory
        """
        try:
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    self.find(item_path)

                search_path = os.path.join(path, self.search_expr)

                if fnmatch.fnmatch(item_path, search_path):
                    self.found_items.append(item_path)

        except FileNotFoundError as e:
            raise ShellFileNotFoundError(
                f"File could not be found: {e} "
            ) from e
        except PermissionError as e:
            raise CommandError(f"Permission denied: {e}") from e
        except NotADirectoryError as e:
            raise CommandError(
                f"Path specified was not a directory: {e}"
            ) from e
        except OSError as e:
            raise CommandError(f"OS Error: {e}") from e

    def run(self) -> int:
        """
        see BaseCommand.run()

        Raises:
            ShellFileNotFoundError: see find()
            CommandError: see find()

        Returns:
            int: exit code of the function (0 for successful)
        """

        self.find(self.path)
        if self.found_items:
            for path in self.found_items:
                self.output.write(f"{path}\n")

        else:
            self.output.write("")

        return 0
