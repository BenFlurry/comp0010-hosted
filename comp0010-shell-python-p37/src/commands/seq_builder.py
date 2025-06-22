"""
module for the seq builder
"""
from io import TextIOBase, StringIO
from typing_extensions import Self
from commands.builder import Builder
from commands.runnable import Runnable
from commands.seq import Seq


class SeqBuilder(Builder):
    """
    a class to build a sequential operator runner
    Args:
        left (CommandBuilder): left command
        right (CommandBuilder): right command
    """

    def __init__(self, left: Builder, right: Builder) -> None:
        self.left: Builder = left
        self.right: Builder = right
        self.in_stream = TextIOBase()
        self.out_stream = TextIOBase()

    def set_in_stream(self, in_stream: TextIOBase) -> Self:
        """
        Sets the in_stream for the command in question
        Args:
            in_stream (StringIO): The input stream for reading data
        """
        self.in_stream = in_stream
        return self

    def set_out_stream(self, out_stream: TextIOBase) -> Self:
        """
        Sets the out_stream for the command in question
        Args:
            in_stream (StringIO): The output stream for reading data
        """
        self.out_stream = out_stream
        return self

    def build(self) -> Runnable:
        """
        Builds a Sequence runnable

        Returns:
            Runnable: the runnable sequence comamnd
        """

        self.left.set_in_stream(self.in_stream)
        self.right.set_in_stream(StringIO())
        self.left.set_out_stream(self.out_stream)
        self.right.set_out_stream(self.out_stream)

        left_runnable = self.left.build()
        right_runnable = self.right.build()
        return Seq(left_runnable, right_runnable)
