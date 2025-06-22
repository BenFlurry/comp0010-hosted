"""
Contains the unit tests for the command helper functions
"""
import unittest
from io import StringIO
from typing import Type
from unittest.mock import MagicMock, mock_open, patch

from parameterized import parameterized

from commands.command_helpers import exception_handled_open, is_stream_empty
from errors.command_errors import CommandError, ShellFileNotFoundError


class TestCommandHelpers(unittest.TestCase):
    """
    Tests the command helpers
    """

    def test_empty_stream(self) -> None:
        """
        Empty streams should be considered empty
        """
        self.assertTrue(is_stream_empty(StringIO()))

    def test_non_seekable_stream(self) -> None:
        """
        Streams that cannot be seeked should not be considered empty
        """
        fake_stream = MagicMock()
        fake_stream.seekable.return_value = False
        self.assertFalse(is_stream_empty(fake_stream))

    def test_stream_with_content(self) -> None:
        """
        Streams with content should not be considered empty. Also, the stream's
        cursor position should be reset
        """
        stream = StringIO()
        stream.write("some string")
        stream.seek(0)
        self.assertFalse(is_stream_empty(stream))
        self.assertEqual(stream.read(), "some string")

    def test_normal_open(self) -> None:
        """
        A normal test to ensure that the file returned works
        """
        mock_file = mock_open(read_data="helloworld")
        with patch('builtins.open', side_effect=mock_file):
            with exception_handled_open(mock_file, "r") as file:
                self.assertEqual(file.read(), "helloworld")

    @parameterized.expand([
        (FileNotFoundError, ShellFileNotFoundError),
        (PermissionError, CommandError),
        (OSError, CommandError)
    ])
    def test_errors(self,
                    open_raised_error: Type[BaseException],
                    shell_raised_error: Type[BaseException]) -> None:
        """
        An erroneous test ensuring that when each of the errors are caught,
        the correct error is re-thrown
        """
        with patch('builtins.open', side_effect=open_raised_error):
            with self.assertRaises(shell_raised_error):
                with exception_handled_open("invalidfile", "r") as _:
                    pass


if __name__ == '__main__':
    unittest.main()
