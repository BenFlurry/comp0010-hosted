"""
A file to unittest the cat shell function
"""
import unittest
from io import StringIO
from unittest.mock import MagicMock, mock_open, patch
from typing import List

from commands.catcommand import CAT
from errors.command_errors import (CommandError, ShellFileNotFoundError,
                                   UnknownFlagError)
from flag import Flag, FlagValue

# pylint: disable=line-too-long


class TestCAT(unittest.TestCase):
    """
    A class to unittest the cat shell function
    """

    def setUp(self) -> None:
        self.in_stream = StringIO()
        self.out_stream = StringIO()

    def _side_effect(self, filename, *_, **__):
        """
        A helper function to mock the open function with different and multiple
        files
        Returns:
            MagicMock: a mock open function
        Raises:
            FileNotFoundError: where the filename cannot be found
        """
        file_contents = {
            'file1.txt': 'Content of file 1',
            'file2.txt': 'Content of file 2',
            'file3.txt': 'Content\nof\nfile\n3'
        }
        if filename in file_contents:
            return mock_open(read_data=file_contents[filename]).return_value
        raise FileNotFoundError(f"No such file: '{filename}'")

    def test_stdin(self) -> None:
        """
        A test to ensure that stdin works
        """
        self.in_stream.write("somefile")
        self.in_stream.seek(0)
        cat = CAT(self.in_stream, self.out_stream, [], [])
        cat.run()
        self.assertEqual(cat.output.getvalue(), self.in_stream.getvalue())

    def test_no_options(self) -> None:
        """
        An erroneous test to ensure that command error is raised with no
        options
        """
        with self.assertRaises(CommandError):
            cat = CAT(self.in_stream, self.out_stream, [], [])
            cat.run()

    def test_invalid_flags(self) -> None:
        """
        An erroneous test to ensure that flags being passed in result in a
        unknown flag error
        """
        flags: List[FlagValue] = [Flag("invalid_flag", "value", "for test")]
        with self.assertRaises(UnknownFlagError):
            cat = CAT(self.in_stream, self.out_stream, flags, [])
            cat.run()

    @patch('builtins.open')
    def test_multiple_options(self, mock_file: MagicMock) -> None:
        """
        Normal test for multiple files (options)

        Arguments:
            mock_file (MagicMock): mock function for __open__ function
        """
        mock_file.side_effect = self._side_effect
        files = ["file1.txt", "file2.txt"]
        cat = CAT(self.in_stream, self.out_stream, [], files)
        cat.run()
        result = cat.output.getvalue()
        self.assertTrue(result,
                        "Content of file 1\nContent of file 2\n")

    def test_file_not_found_error(self) -> None:
        """
        An erroneous test where a file does not exist
        """
        options = ["invalid_file.txt"]
        with patch("builtins.open", side_effect=FileNotFoundError):
            with self.assertRaises(ShellFileNotFoundError):
                cat = CAT(self.in_stream, self.out_stream, [], options)
                cat.run()

    def test_file_permission_error(self) -> None:
        """
        An erroneous test where a file does not have permission to be
        opened
        """
        options = ["invalid_file.txt"]
        with patch("builtins.open", side_effect=PermissionError):
            with self.assertRaises(CommandError):
                cat = CAT(self.in_stream, self.out_stream, [], options)
                cat.run()

    def test_os_error(self) -> None:
        """
        An erroneous test where a file does not have permission to be
        opened
        """
        options = ["invalid_file.txt"]
        with patch("builtins.open", side_effect=OSError):
            with self.assertRaises(CommandError):
                cat = CAT(self.in_stream, self.out_stream, [], options)
                cat.run()


if __name__ == "__main__":
    unittest.main()
