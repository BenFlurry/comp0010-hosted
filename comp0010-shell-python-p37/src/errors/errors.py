"""
Base error module representing all errors understandable by the shell
"""
from abc import ABC


class BaseShellError(ABC, Exception):
    """
    Represents a basic error understood and thrown by the shell.

    This error, by design, should never be thrown directly;
    a subclass must implement it.
    """
    def __init__(self, message: str = 'Unknown') -> None:
        self.message = message

    def __str__(self) -> str:
        return f"{type(self).__name__}: {self.message}"  # pragma: no cover
