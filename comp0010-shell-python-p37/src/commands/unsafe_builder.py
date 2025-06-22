"""
Package that contains a class that can build a command
"""

from io import StringIO, TextIOBase

from typing_extensions import Self

from errors.errors import BaseShellError

from .builder import Builder
from .forwarder import Forwarder
from .runnable import Runnable
from .unsafe_decorator import UnsafeDecorator


class UnsafeBuilder(Builder):
    """
    A decorator around any builder.

    Builds an unsafe variant of the underlying builder. This wraps the final
    runnable in an Unsafe wrapper.
    """
    def __init__(self, builder: Builder) -> None:
        self.in_stream: TextIOBase = StringIO()
        self.out_stream: TextIOBase = StringIO()
        self.wrapped_builder = builder

    def set_in_stream(self, in_stream: TextIOBase) -> Self:
        self.in_stream = in_stream
        return self

    def set_out_stream(self, out_stream: TextIOBase) -> Self:
        self.out_stream = out_stream
        return self

    def build(self) -> Runnable:
        """
        Calls the super class' build, and wraps it around an unsafe decorator.

        If initializing the underlying Command object causes an error, a
        Forwarder runnable is created instead.

        Returns:
            Runnable: A built runnable.
        """
        self.wrapped_builder.set_in_stream(self.in_stream)
        self.wrapped_builder.set_out_stream(self.out_stream)
        try:
            return UnsafeDecorator(
                self.wrapped_builder.build(), self.out_stream)
        except BaseShellError as e:
            return Forwarder(e.message, self.out_stream, 1)
