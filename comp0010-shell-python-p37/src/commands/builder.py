"""
Interface: The builder interface for multiple builders available.

Intended for:
- CommandBuilder
- PipeBuilder
- SeqBuilder
"""

from abc import ABC, abstractmethod
from io import TextIOBase

from typing_extensions import Self

from .runnable import Runnable


# Disabled because this class is intentionally short.
# pylint: disable=too-few-public-methods
# Coverage disabled because this is an interface
class Builder(ABC):
    """
    The builder interface for the multiple builders available for shell. This
    class only has a single method, build().

    Build() must produce a Runnable.

    Building should be done recursively; builders can take in other builders if
    it is convenient to complete a command expression.
    """
    @abstractmethod
    def build(self) -> Runnable:  # pragma: no cover
        """
        Builds a runnable.

        Returns:
            Runnable: A runnable object
        """
        raise NotImplementedError('subclasses should implement this class')

    @abstractmethod
    def set_in_stream(self, in_stream: TextIOBase) -> Self:  # pragma: no cover
        """
        Sets the in_stream for the command in question

        Args:
            in_stream (StringIO): The input stream for reading data
        """
        raise NotImplementedError('subclasses should implement this class')

    @abstractmethod
    def set_out_stream(self,
                       out_stream: TextIOBase) -> Self:  # pragma: no cover
        """
        Sets the out_stream for the command in question

        Args:
            out_stream (StringIO): The output stream for writing data
        """
        raise NotImplementedError('subclasses should implement this class')
