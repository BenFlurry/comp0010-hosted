"""
Some helper functions for the commands to use
"""

from io import TextIOWrapper, SEEK_SET, SEEK_END
from typing import cast
from errors.command_errors import ShellFileNotFoundError, CommandError


def is_stream_empty(stream: TextIOWrapper) -> bool:
    """
    Checks if the stream is empty using arbitrary heuristics.

    Heuristics: If the stream is not seekable, we can't tell, so we say it is
    not empty. If the stream is seekable, and there is still content towards
    the end of the stream, then the stream is not empty. Otherwise, it is
    empty.
    """
    if not stream.seekable():
        return False

    pos = stream.tell()
    stream.seek(0, SEEK_END)
    endpos = stream.tell()
    stream.seek(pos, SEEK_SET)
    return endpos == pos


def exception_handled_open(file: str, open_mode: str) -> TextIOWrapper:
    """
    This function is used in place of with open(), with automatic error
    handling to prevent the need for the command to handle file open errors

    Arguments:
        file (str): the name or path of the file to be opened
        open_mode (str): 'r' or 'w' defining the readability of the opened file

    Raises:
        ShellFileNotFoundError: if the file specified cannot be found in the
            path or directory
        CommandError: if permission is denied, or an OS Error occurs

    Returns:
        TextIOWrapper: an opened IO file object
    """
    try:
        # The open function returns an IO[Any] object, which has the same
        # methods as TextIOWrapper, but clashes with our type checking.
        # Therefore, we cast it to TextIOWrapper.

        return cast(TextIOWrapper,  open(file, open_mode, encoding='utf-8'))

    except FileNotFoundError as e:
        raise ShellFileNotFoundError(
            f"{file} file could not be found: {e}"
        ) from e

    except PermissionError as e:
        raise CommandError(
            f"unauthorised access to file {file}: {e}"
        ) from e

    except OSError as e:
        raise CommandError(
            f"OS Error opening {file}: {e}"
        ) from e
