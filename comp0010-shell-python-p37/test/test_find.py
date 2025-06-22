"""
A module that contains unit tests for the find command.
"""
import unittest
from io import StringIO
from typing import List
from unittest.mock import patch, MagicMock

from commands.findcommand import Find
from errors.command_errors import (CommandError, ShellFileNotFoundError,
                                   UnknownFlagError, UnknownFlagValueError)
from errors.error_dsi import DeveloperSkillIssue
from flag import Flag, FlagValue


class TestFind(unittest.TestCase):
    """
    A test class for the Echo class.
    """

    def setUp(self) -> None:
        self.in_stream = StringIO()
        self.out_stream = StringIO()

    def tearDown(self) -> None:
        self.in_stream.close()
        self.out_stream.close()

    # -- TESTING FLAGS --
    def test_valid_flags(self) -> None:
        """
        A normal test checking that a valid flag input creates
        """
        flags: List[FlagValue] = [Flag("name", "expr", "Test")]
        f = Find(self.in_stream, self.out_stream, flags, [])
        self.assertEqual(f.search_expr, "expr")

    def test_invalid_flag_name(self) -> None:
        """
        An erroneous test for a flag with the wrong flagname
        """
        flags: List[FlagValue] = [Flag("", "expr", "Test")]
        with self.assertRaises(DeveloperSkillIssue):
            Find(self.in_stream, self.out_stream, flags, [])

    def test_invalid_flag_value_type(self) -> None:
        """
        An erroneous test for invalid flag value type
        """
        flags: List[FlagValue] = [Flag("name", 1, "Test")]
        with self.assertRaises(UnknownFlagValueError):
            Find(self.in_stream, self.out_stream, flags, [])

    def test_invalid_number_flags(self) -> None:
        """
        An erroneous test for where more than 1 flag is provided
        """
        flags: List[FlagValue] = [Flag("name", "hi", "Test"),
                                  Flag("name", "hello", "Test")]
        with self.assertRaises(UnknownFlagError):
            Find(self.in_stream, self.out_stream, flags, [])

    def test_no_flag(self) -> None:
        """
        A normal test checking that no flag uses wildcard *.*
        """
        # flags = [Flag("name", "hi", "Test")]
        f = Find(self.in_stream, self.out_stream, [], [])
        self.assertEqual(f.search_expr, "*")

    # -- TESTING OPTIONS --
    def test_invalid_number_of_options(self) -> None:
        """
        An erroneous test for a number of options that is more than 1
        """
        options = ["path1", "path2"]
        with self.assertRaises(CommandError):
            Find(self.in_stream, self.out_stream, [], options)

    def test_invalid_option_value(self) -> None:
        """
        An erroneous test for where the option specified isn't a valid path
        """
        options = ["path1"]
        with patch("os.path.exists", return_value=False):
            with self.assertRaises(CommandError):
                Find(self.in_stream, self.out_stream, [], options)

    def test_valid_option(self) -> None:
        """
        A normal test for where 0 options are provided
        """
        f = Find(self.in_stream, self.out_stream, [], [])
        self.assertEqual(f.path, ".")

    def test_valid_options(self) -> None:
        """
        A normal test for where 1 option is provided
        """
        options = ["path"]
        with patch("os.path.exists", return_value=True):
            f = Find(self.in_stream, self.out_stream, [], options)
            self.assertEqual(f.path, "path")

    # -- NORMAL TEST --
    def test_normal_wildcard_valid_flags(self) -> None:
        """
        A normal test for where wild cards are used in the filename flag
        """
        flags: List[FlagValue] = [Flag("name", "*.py", "Test")]
        with patch("os.listdir", return_value=["txt1.py", "txt2.py", "dir"]), \
            patch("os.getcwd", return_value=""), \
            patch("os.path.join", side_effect=lambda _, p: p), \
                patch("os.path.isdir", return_value=False):
            f = Find(self.in_stream, self.out_stream, flags, [])
            f.run()
            self.assertEqual(f.search_expr, "*.py")
            self.assertEqual(f.output.getvalue(), "txt1.py\ntxt2.py\n")

    def test_normal_no_wildcard_valid_flags(self) -> None:
        """
        A normal test, with no wild cards in the flag value
        """
        flags: List[FlagValue] = [Flag("name", "txt1.py", "Test")]
        with patch("os.listdir", return_value=["txt1.py", "txt2.py", "dir"]), \
            patch("os.getcwd", return_value=""), \
            patch("os.path.join", side_effect=lambda _, p: p), \
                patch("os.path.isdir", return_value=False):
            f = Find(self.in_stream, self.out_stream, flags, [])
            f.run()
            self.assertEqual(f.output.getvalue(), "txt1.py\n")

    def test_normal_no_found_items(self) -> None:
        """
        A normal test for where the directory specified does not contain any
        files matching the flag value
        """
        flags: List[FlagValue] = [Flag("name", "txt3.py", "Test")]
        with patch("os.listdir", return_value=["txt1.py", "txt2.py", "dir"]), \
            patch("os.getcwd", return_value=""), \
            patch("os.path.join", side_effect=lambda _, p: p), \
                patch("os.path.isdir", return_value=False):
            f = Find(self.in_stream, self.out_stream, flags, [])
            f.run()
            self.assertEqual(f.output.getvalue(), "")

    def test_normal_with_recursion(self) -> None:
        """
        A normal test testing the recursive element of the _find function
        """
        flags: List[FlagValue] = [Flag("name", "txt3.py", "Test")]
        listdir_mock = [["dir"], ["txt1.py"], ["txt2.py"]]
        with patch("os.listdir", side_effect=iter(listdir_mock)), \
            patch("os.getcwd", return_value=""), \
            patch("os.path.join", side_effect=lambda _, i: i), \
                patch("os.path.isdir", side_effect=lambda d: d == "dir"):
            f = Find(self.in_stream, self.out_stream, flags, [])
            f.run()
            self.assertEqual(f.output.getvalue(), "")

    def test_file_not_found(self) -> None:
        """
        An erroneous test for where the file specified by the path option can't
        be found
        """
        with patch("os.listdir", side_effect=FileNotFoundError):
            with self.assertRaises(ShellFileNotFoundError):
                Find.find(MagicMock(), "file_isn't_here")

    def test_permission_error(self) -> None:
        """
        An erroneous test for where permission is denied when accessing a file
        """
        with patch("os.listdir", side_effect=PermissionError):
            with self.assertRaises(CommandError):
                Find.find(MagicMock(), "unauthorised_path")

    def test_not_a_directory_error(self) -> None:
        """
        An erroneous test for where the specified path option is not a
        directory
        """
        with patch("os.listdir", side_effect=NotADirectoryError):
            with self.assertRaises(CommandError):
                Find.find(MagicMock(), "not_a_directory.txt")

    def test_oserror(self) -> None:
        """
        An erroneous test for where os error
        """
        with patch("os.listdir", side_effect=OSError):
            with self.assertRaises(CommandError):
                Find.find(MagicMock(), "not_a_directory.txt")


if __name__ == "__main__":
    unittest.main()
