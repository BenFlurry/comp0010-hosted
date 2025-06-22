"""
A file for testing the ls command using the unittest module
"""
import unittest
from io import StringIO
from unittest.mock import patch

from commands.lscommand import LS
from errors.command_errors import (CommandError, ShellFileNotFoundError,
                                   ShellNotADirectoryError)
from flag import Flag


class TestLS(unittest.TestCase):
    """
    A unit test class for testing the ls command in src.commands.lscommand.py
    """

    def setUp(self) -> None:
        self.in_stream = StringIO()
        self.out_stream = StringIO()

    def test_too_many_options(self) -> None:
        """
        A test to ensure that if more than 1 option is passed in, a command
        error is raised
        """
        options = ["dir1", "dir2"]
        with self.assertRaises(CommandError):
            LS(self.in_stream, self.out_stream, [], options).run()

    def test_invalid_flags(self) -> None:
        """
        A test to ensure that if flags are passed in to the ls command, a
        command error is raised
        """
        flags = [Flag("some_name", "some_val", "for testing")]
        with self.assertRaises(CommandError):
            LS(self.in_stream, self.out_stream, flags, []).run()

    def test_no_options_with_hidden(self) -> None:
        """
        A test to ensure that when no options are passed, os.getcwd is ran
        """
        directory = ["file1.py", ".hidden.py", "dir"]
        with patch("os.getcwd", return_value=""), patch(
            "os.path.isdir", return_value=True
        ), patch("os.listdir", return_value=directory):
            ls = LS(self.in_stream, self.out_stream, [], [])
            ls.run()
            self.assertEqual(ls.output.getvalue(), "file1.py\tdir\t\n")

    def test_option_isnt_a_directory(self) -> None:
        """
        A test for where the option passed is not a valid directory
        """
        options = ["not_a_dir.txt"]
        with patch("os.listdir", side_effect=NotADirectoryError), \
             self.assertRaises(ShellNotADirectoryError):
            LS(self.in_stream, self.out_stream, [], options).run()

    def test_option_no_permission(self) -> None:
        """
        A test for where the option cannot be accessed
        """
        options = ["not_a_dir.txt"]
        with patch("os.listdir", side_effect=PermissionError), \
             self.assertRaises(CommandError):
            LS(self.in_stream, self.out_stream, [], options).run()

    def test_option_os_error(self) -> None:
        """
        A test for where the option passed gives an OS Error
        """
        options = ["not_a_dir.txt"]
        with patch("os.listdir", side_effect=OSError), \
             self.assertRaises(CommandError):
            LS(self.in_stream, self.out_stream, [], options).run()

    def test_option_file_not_found(self) -> None:
        """
        A test for where the option passed cannot be found
        """
        options = ["not_a_dir.txt"]
        with patch("os.listdir", side_effect=FileNotFoundError), \
             self.assertRaises(ShellFileNotFoundError):
            LS(self.in_stream, self.out_stream, [], options).run()


if __name__ == "__main__":
    unittest.main()
