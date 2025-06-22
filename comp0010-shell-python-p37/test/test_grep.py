"""
Module to test the grep command
"""
import unittest
from io import StringIO
from typing import List
from unittest.mock import mock_open, patch

from commands.grepcommand import Grep
from errors.command_errors import CommandError, ShellFileNotFoundError
from flag import FlagValue


class TestGrep(unittest.TestCase):
    """
    Class to test the grep command
    """

    def setUp(self) -> None:
        self.in_stream = StringIO()
        self.out_stream = StringIO()
        self.pattern = "line"
        self.files = ["file1.txt", "file2.txt"]
        self.mock_file = mock_open(read_data="line1\n12345\n\n\n   test\n")

    def tearDown(self) -> None:
        """
        Closes the streams
        """
        self.in_stream.close()
        self.out_stream.close()

    def _open_helper(
        self,
        flags: List[FlagValue],
        options: List[str],
        expected_output: str,
    ) -> None:
        """
        Helper function to open a file
        """
        with patch("builtins.open", self.mock_file):
            grep = Grep(self.in_stream, self.out_stream, flags, options)
            result = grep.run()
            self.assertEqual(self.out_stream.getvalue(), expected_output)
            self.assertEqual(result, 0)

    def test_grep_normal(self) -> None:
        """
        Tests the grep command with a normal pattern and file
        """
        options = [self.pattern, self.files[0]]
        self._open_helper([], options, "line1\n")

    def test_grep_stdin(self) -> None:
        """
        Tests the grep command with stdin
        """
        self.in_stream.write("line1\n12345\n\n\n   test\n")
        self.in_stream.seek(0)
        options = [self.pattern]
        Grep(self.in_stream, self.out_stream, [], options).run()
        self.assertEqual(self.out_stream.getvalue(), "line1\n")

    def test_grep_multiple_files(self) -> None:
        """
        Tests the grep command with multiple files
        """
        options = [self.pattern] + self.files
        self._open_helper([], options, "file1.txt:line1\nfile2.txt:line1\n")

    def test_grep_file_not_found(self) -> None:
        """
        Tests the grep command with a non-existent file
        """
        options = [self.pattern, self.files[0]]
        with self.assertRaises(ShellFileNotFoundError):
            Grep(self.in_stream, self.out_stream, [], options).run()

    def test_grep_permissions_denied(self) -> None:
        """
        Tests the grep command with a file that has no read permissions
        """
        options = [self.pattern, self.files[0]]
        with patch("builtins.open", side_effect=PermissionError):
            with self.assertRaises(CommandError):
                Grep(self.in_stream, self.out_stream, [], options).run()

    def test_grep_os_error(self) -> None:
        """
        Tests the grep command with a file that has no read permissions
        """
        options = [self.pattern, self.files[0]]
        with patch("builtins.open", side_effect=OSError):
            with self.assertRaises(CommandError):
                Grep(self.in_stream, self.out_stream, [], options).run()

    def test_grep_no_pattern(self) -> None:
        """
        Tests the grep command with no pattern
        """
        options = [self.files[0]]
        with self.assertRaises(CommandError):
            Grep(self.in_stream, self.out_stream, [], options).run()

    def test_grep_invalid_pattern(self) -> None:
        """
        Tests the grep command with an invalid pattern
        """
        options = ["[", self.files[0]]
        with self.assertRaises(CommandError):
            Grep(self.in_stream, self.out_stream, [], options)

    def test_grep_no_files(self) -> None:
        """
        Tests the grep command with no files
        """
        options = [self.pattern]
        with self.assertRaises(CommandError):
            Grep(self.in_stream, self.out_stream, [], options).run()

    def test_grep_tabs(self) -> None:
        """
        Tests the grep command with leading spaces
        """
        pattern = "test"
        options = [pattern, self.files[0]]
        self._open_helper([], options, "   test\n")


if __name__ == "__main__":
    unittest.main()
