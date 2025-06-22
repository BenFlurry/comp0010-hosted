"""
Consists of errors thrown by redirect
"""
# Disable lint for too few public methods, these are
# errors we want a specific object for
# pylint: disable=too-few-public-methods

from .errors import BaseShellError


class RedirectError(BaseShellError):
    """
    Represents a base command error. All command errors
    will inherit from this class.
    """
    def __str__(self) -> str:
        return f'Redirect Error: {self.message}'
