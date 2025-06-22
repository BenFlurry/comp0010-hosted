"""
Imports the base commmand, and implements the interface for the ls command
"""
import os

from commands.base_command import BaseCommand
from commands.command_spec import CommandSpecification
from errors.command_errors import CommandError, ShellNotADirectoryError, \
    ShellFileNotFoundError


class LS(BaseCommand):
    """
    class for the ls command, which implements the BaseCommand interface
    Initializes the CD object with input and output streams.

    """

    COMMAND_SPECIFICATION = CommandSpecification(
        "ls", [], ("[PATH]", "Prints all files in the directory")
    )

    def run(self) -> int:
        """
        see BaseCommand.run()
        Raises:
            ShellFileNotFoundError: if the given directory cannot be found
            CommandError: if the directory is unaccessible or OSError
            ShellNotADirectoryError: if the directory is not a directory

        Returns:
            int: exit code of the function (0 if successful)
        """
        if len(self.options) > 1:
            raise CommandError("ls command only takes 0 or 1 options")
        if self.flags:
            raise CommandError("ls command does not have any flags")
        if len(self.options) == 0:
            ls_directory = os.getcwd()
        else:
            ls_directory = self.options[0]

        try:
            for file in os.listdir(ls_directory):
                if not file.startswith("."):
                    self.output.write(f"{file}\t")
        except FileNotFoundError as e:
            raise ShellFileNotFoundError(
                f"{ls_directory} is not a valid directory: {e}"
            ) from e

        except PermissionError as e:
            raise CommandError(
                f"{ls_directory} cannot be opened: {e}"
            ) from e

        except NotADirectoryError as e:
            raise ShellNotADirectoryError(
                f"{ls_directory} is not a directory; {e}"
            ) from e
        except OSError as e:
            raise CommandError(
                f"{ls_directory} caused an OSError: {e}"
            ) from e

        self.output.write('\n')
        return 0
