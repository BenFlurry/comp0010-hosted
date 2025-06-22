"""
Interface: Implements a Runnable class. See documentation of Runnable for more
information.
"""
from abc import ABC, abstractmethod
from types import TracebackType
from typing import ContextManager, Optional, Type

from typing_extensions import Literal, Self


# Coverage disabled because this is an interface
class Runnable(ContextManager, ABC):
    """
    A runnable. Represents an enclosed context that can be executed by a
    runner. This class exists within the commands package, but should be
    extended for use within shell features such as pipes and command
    substitution.

    This class has 2 attributes: The input and output StringIOs
    """
    @abstractmethod
    def run(self) -> int:  # pragma: no cover
        """
        Executes the representation of the runnable once.
        """
        raise NotImplementedError(
            'this function is meant to be re-implemented')

    @abstractmethod
    def close(self) -> None:  # pragma: no cover
        """
        Closes all the resources used by this runnable. If you find yourself
        calling this, consider using the context manager.

        If this is being run from the root, run with runnable.run_and_close()
        """
        raise NotImplementedError(
            'this function is meant to be re-implemented'
        )

    def run_and_close(self) -> int:
        """
        Runs the command and closes all resources immediately after.
        """
        with self as r:
            return r.run()

    def __enter__(self) -> Self:
        return self

    def __exit__(self,
                 exception_type: Optional[Type[BaseException]],
                 exception_value: Optional[BaseException],
                 traceback: Optional[TracebackType]) -> Literal[False]:
        self.close()
        return False  # propagate errors
