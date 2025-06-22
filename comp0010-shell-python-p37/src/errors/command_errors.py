"""
Consists of errors thrown by commands
"""
# Disable lint for too few public methods, these are
# errors we want a specific object for
# pylint: disable=too-few-public-methods

from .errors import BaseShellError


class CommandError(BaseShellError):
    """
    Represents a base command error. All command errors
    will inherit from this class.
    """
    def __str__(self) -> str:
        return f'Command, {type(self).__name__}: {self.message}'


class UnknownFlagError(CommandError):
    """
    Represents an error when a flag is not known to the command
    """


class UnknownFlagValueError(CommandError):
    """
    Represents an error when a flag value is not one of the expected
    values
    """


class ShellFileNotFoundError(CommandError):
    """
    Represents an error when a file is not found
    """


class ShellNotADirectoryError(CommandError):
    """
    Represents an error when a path is not a directory
    """
