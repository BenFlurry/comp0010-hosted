"""
Consists of shell errors thrown by the shell
"""
# Disable lint for too few public methods, these are
# errors we want a specific object for
# pylint: disable=too-few-public-methods

from .errors import BaseShellError


class ShellExitError(BaseShellError):
    """
    Represents an error when the shell should exit
    """
