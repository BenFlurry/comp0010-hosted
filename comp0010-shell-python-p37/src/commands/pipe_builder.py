"""
Builds a pipe when given either two command builders or a pipe builder and a
command builder.
"""
from io import StringIO
from typing_extensions import Self

from errors import check_arguments

from commands.builder import Builder
from commands.runnable import Runnable
from commands.pipe import Pipe


class PipeBuilder(Builder):
    """
    Builds a pipe

    Args:
        left (T): The left command or pipe builder
        right (T): The right command
    """

    @check_arguments
    def __init__(self, left: Builder, right: Builder) -> None:
        self.left: Builder = left
        self.right: Builder = right
        self.in_stream: StringIO = StringIO()
        self.out_stream: StringIO = StringIO()
        self.mid_stream: StringIO = StringIO()
        self.left_runnable: Runnable
        self.right_runnable: Runnable

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

    def build(self) -> Pipe:
        """
        Builds a pipe

        Returns:
            Builder: A pipe
        """
        self.left.set_in_stream(self.in_stream)
        self.left.set_out_stream(self.mid_stream)
        self.right.set_in_stream(self.mid_stream)
        self.right.set_out_stream(self.out_stream)

        self.left_runnable = self.left.build()
        self.right_runnable = self.right.build()

        return Pipe(self.left_runnable, self.right_runnable, self.mid_stream)
