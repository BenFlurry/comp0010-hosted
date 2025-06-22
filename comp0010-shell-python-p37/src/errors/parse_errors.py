"""
Consists of errors thrown by commands
"""
# Disable lint for too few public methods, these are
# errors we want a specific object for
# pylint: disable=too-few-public-methods

from .errors import BaseShellError


class ParseError(BaseShellError):
    """
    Represents a base command error. All command errors
    will inherit from this class.
    """

    def __str__(self) -> str:
        return f"Command, {type(self).__name__}: {self.message}"


class NoCommandError(ParseError):
    """
    Represents an error when there isn't anything on the command line.
    (Ideally, the shell can check the input string first)
    """


class UnknownCommandError(ParseError):
    """
    Represents an error when a command is not known to the parser
    """


class UnknownFlagError(ParseError):
    """
    Represents an error when a flag is not known to the parser
    """


class UnknownFlagValueError(ParseError):
    """
    Represents an error when a flag value is not one of the expected
    values
    """


class UserParseError(ParseError):
    """
    Represents an error when a user input is not valid
    """
