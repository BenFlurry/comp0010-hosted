"""
Imports BaseCommand interface and implements it with the cd command
"""

import os
from io import StringIO
from typing import List

from errors.command_errors import CommandError, ShellFileNotFoundError, \
    ShellNotADirectoryError
from errors.error_dsi import DeveloperSkillIssue
from flag import FlagValue

from commands.base_command import BaseCommand
from commands.command_spec import CommandSpecification


class CD(BaseCommand):
    """
    class for the cd command, which implements the BaseCommmand interface
    """
    COMMAND_SPECIFICATION = \
        CommandSpecification("cd", [], (
            "PATH", "Change the current working directory\n  "
            "PATH is a relative path to the target directory"))

    def __init__(self, in_stream: StringIO, out_stream: StringIO,
                 flags: List[FlagValue], options: List[str]) -> None:
        """
        Initializes the CD object with in_stream and out_stream streams.

        Args:
            in_stream (StringIO): Input stream for the command.
            out_stream (StringIO): Output stream for the command.
            flags (List[FlagValue]): List of flags supported by the command.
            options (List[str]): List of options supported by the command.
        """

        self.path = ''
        self._check_flags_guard(options)
        super().__init__(in_stream, out_stream, flags, options)

    def _check_flags_guard(self, options: List[str]):
        if not len(options) == 1:
            raise CommandError(
                'only one option is accepted for cd')
        self.path = options[0]
        if not os.path.exists(self.path):
            raise ShellFileNotFoundError()
        if not os.path.isdir(self.path):
            raise ShellNotADirectoryError(f'{self.path} is not a directory')

    def run(self) -> int:
        """
        see BaseCommand.run()
        """
        try:
            os.chdir(self.options[0])
        except FileNotFoundError as e:
            raise DeveloperSkillIssue('dir not found. missed checks?') from e
        except NotADirectoryError as e:
            raise DeveloperSkillIssue('not a dir. missed checks?') from e
        except PermissionError as e:
            raise CommandError(
                'process does not have permission to open the file') from e
        except OSError as e:
            raise DeveloperSkillIssue('unknown OSError') from e
        return 0
