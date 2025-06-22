"""
Imports the base commmand, and implements the interface for the pwd command
"""
import os

from commands.base_command import BaseCommand
from commands.command_spec import CommandSpecification
from errors.command_errors import CommandError, ShellFileNotFoundError, \
    ShellNotADirectoryError


class Pwd(BaseCommand):
    """
    Gets the parent working directory.
    """
    COMMAND_SPECIFICATION = \
        CommandSpecification(
            "pwd", [], ("", "Outputs the current working directory"))

    def run(self) -> int:
        """
        see BaseCommand.run()
        Raises:
            CommandError: if permission is denied, or an OS Error is thrown
            ShellNotADirectoryError: if the directory given is not a directory
            SheLlFileNotFoundError: if the file cannot be found

        Returns:
            int: exit code of the function (0 if successful)
        """
        try:
            self.output.write(os.getcwd() + "\n")
            return 0
        except FileNotFoundError as e:
            raise ShellFileNotFoundError(f"Error: {e} (File not found)") from e
        except NotADirectoryError as e:
            raise ShellNotADirectoryError(f"Error: {e} (Not a directory)") \
                from e
        except PermissionError as e:
            raise CommandError(f"Error: {e} (Permission denied)") from e
        except OSError as e:
            raise CommandError(f"Error: {e} (General OS error)") from e
