"""
Builds a command when given flags and options
"""
from io import StringIO, TextIOBase
from typing import List, Type

from typing_extensions import Self

from errors import check_arguments
from flag import FlagValue

from .base_command import BaseCommand
from .runnable import Runnable
from .builder import Builder


class CommandBuilder(Builder):
    """
    Builds a command.

    Args:
        command_type (Type[T]): The type of command that this handler will
                                work with.
    """
    @check_arguments
    def __init__(self, command_type: Type[BaseCommand]) -> None:
        self.command_type = command_type
        self.flags: List[FlagValue] = []
        self.options: List[str] = []
        self.in_stream: TextIOBase = StringIO()
        self.out_stream: TextIOBase = StringIO()

    @check_arguments
    def set_in_stream(self, in_stream: StringIO) -> Self:
        """
        Sets the in_stream for the command in question

        Args:
            in_stream (StringIO): The input stream for reading data
        """
        self.in_stream = in_stream
        return self

    @check_arguments
    def set_out_stream(self, out_stream: StringIO) -> Self:
        """
        Sets the out_stream for the command in question

        Args:
            out_stream (StringIO): The output stream for writing data
        """
        self.out_stream = out_stream
        return self

    def add_flag(self, flag: FlagValue) -> Self:
        """
        Adds a flag to the command builder.

        Args:
            flag (FlagValue): The flag to add.
        """
        self.flags.append(flag)
        return self

    def add_option(self, option: str) -> Self:
        """
        Adds an option to the command builder

        Args:
            option (str): The option to add.
        """
        self.options.append(option)
        return self

    def build(self) -> Runnable:
        """
        Builds the command from the added flags and options.

        Returns:
            value (Runnable): A built runnable.
        """
        command = self.command_type(
            self.in_stream, self.out_stream, self.flags, self.options)
        return command
