"""
This module tests the Exit command.
"""
import unittest
from io import StringIO

from commands.exitcommand import Exit
from errors.shell_errors import ShellExitError


class TestExit(unittest.TestCase):
    """
    A test class for the Exit class.
    """
    def setUp(self):
        """
        Set up the test class.
        """
        self.in_stream = StringIO()
        self.out_stream = StringIO()

    def test_exit(self):
        """
        Test the Exit class.
        """
        exit_command = Exit(self.in_stream, self.out_stream, [], [])
        with self.assertRaises(ShellExitError):
            exit_command.run()
