"""
A module that contains unit tests for the echo command.
"""
import unittest
from io import StringIO
from unittest.mock import patch

from commands.pwdcommand import Pwd
from errors.command_errors import CommandError, ShellFileNotFoundError, \
    ShellNotADirectoryError


class TestPwd(unittest.TestCase):
    """
    A test class for the Pwdlass.
    """

    def setUp(self):
        # Create StringIO streams for testing
        self.in_stream = StringIO()
        self.out_stream = StringIO()

    def test_pwd_normal(self):
        """
        Test the pwd command with a single option.
        """
        flags = []
        options = []
        with patch("os.getcwd", return_value="/home/user"):
            pwd = Pwd(self.in_stream, self.out_stream, flags, options)
            result = pwd.run()
            self.assertEqual(pwd.output.getvalue(), "/home/user\n")
            self.assertEqual(result, 0)

    def test_pwd_file_not_found(self):
        """
        Test the pwd command assuming the current directory is a path that does
        not exist.
        """
        with self.assertRaises(ShellFileNotFoundError):
            with patch("os.getcwd", side_effect=FileNotFoundError):
                pwd_command = Pwd(self.in_stream, self.out_stream, [], [])
                pwd_command.run()

    def test_pwd_not_a_directory(self):
        """
        Test the pwd command assuming the current directory is a file.
        """
        with self.assertRaises(ShellNotADirectoryError):
            with patch("os.getcwd", side_effect=NotADirectoryError):
                pwd_command = Pwd(self.in_stream, self.out_stream, [], [])
                pwd_command.run()

    def test_pwd_permission_denied(self):
        """
        Test the pwd command assuming the current directory is a path that the
        user does not have permission to access.
        """
        with self.assertRaises(CommandError):
            with patch("os.getcwd", side_effect=PermissionError):
                pwd_command = Pwd(self.in_stream, self.out_stream, [], [])
                pwd_command.run()

    def test_pwd_oserror(self):
        """
        Test the pwd command assuing that os.getcwd() raises an OSError.
        """
        with self.assertRaises(CommandError):
            with patch("os.getcwd", side_effect=OSError):
                pwd_command = Pwd(self.in_stream, self.out_stream, [], [])
                pwd_command.run()


if __name__ == "__main__":
    unittest.main()
