"""
This module contains the SHellError class, which is used to raise errors
properly
"""
from antlr4 import error  # type: ignore

from errors.parse_errors import UserParseError
# pylint: disable=too-few-public-methods, too-many-arguments


class ShellErrorListener(error.ErrorListener.ErrorListener):
    """
    Error Listener for the parser. This is used to replace fuctionality of the
    default error listener, which is to print to stderr.
    """

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise UserParseError("Syntax Error: " + msg) from e
