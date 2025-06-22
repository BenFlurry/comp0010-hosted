"""
A redirect builder, where files are redirected.
"""

# The encoding of the file doesn't matter to the builder
# pylint: disable=consider-using-with

from io import StringIO
from os import PathLike
from typing import Optional

from typing_extensions import Self

from errors import check_arguments
from errors.redirect_errors import RedirectError
from errors.command_errors import ShellFileNotFoundError
from flag import FlagValue

from .command_builder import CommandBuilder
from .redirect import Redirect
from .runnable import Runnable


class RedirectBuilder(CommandBuilder):
    """
    Redirect builders are special builders that don't produce its own object;
    instead, it decorates the underlying builder's input and output stream
    directly.

    Arguments:
        child_buildable (CommandBuilder): The child buildable for the redirect
                                          builder to wrap around
    """

    @check_arguments
    def __init__(self, child_buildable: CommandBuilder) -> None:
        super().__init__(child_buildable.command_type)

        self.child_buildable: CommandBuilder = child_buildable
        self.in_file: Optional[PathLike] = None
        self.out_file: Optional[PathLike] = None

    @check_arguments
    def set_in_file(self, in_file: PathLike) -> Self:
        """
        Sets the input file. This takes precedence over in_stream.

        Arguments:
            in_file (PathLike): A path to a file name.
        """
        self.in_file = in_file
        return self

    @check_arguments
    def set_out_file(self, out_file: PathLike) -> Self:
        """
        Sets the output file. This takes precedence over in_stream.

        Arguments:
            out_file (PathLike): A path to a file name.
        """
        self.out_file = out_file
        return self

    def add_flag(self, flag: FlagValue) -> Self:
        """
        Adds a flag to the command builder.

        Args:
            flag (FlagValue): The flag to add.
        """
        self.child_buildable.add_flag(flag)
        return self

    def add_option(self, option: str) -> Self:
        """
        Adds an option to the command builder

        Args:
            option (str): The option to add.
        """
        self.child_buildable.add_option(option)
        return self

    def build(self) -> Runnable:
        # The closure of the following streams are handled by the runnables
        try:
            target_in = open(self.in_file) if self.in_file is not None \
                else self.in_stream
            target_out = open(self.out_file, 'w') if self.out_file is not None\
                else self.out_stream
        except FileNotFoundError as e:
            raise ShellFileNotFoundError from e
        except PermissionError as e:
            raise RedirectError('unable to open one of the files') from e
        except IsADirectoryError as e:
            raise RedirectError('unexpected directory') from e
        except OSError as e:
            raise RedirectError('unknown error') from e

        child_in, child_out = StringIO(), StringIO()
        return Redirect(target_in,
                        target_out,
                        child_in,
                        child_out,
                        self.child_buildable
                        .set_in_stream(child_in)
                        .set_out_stream(child_out)
                        .build())
