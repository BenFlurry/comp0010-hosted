"""
A module that contains unit tests for the echo command.
"""
import unittest
from io import StringIO
from unittest.mock import mock_open, patch
from typing import List, Optional, Type

from parameterized import parameterized

from commands.tailcommand import Tail
from errors.command_errors import CommandError, ShellFileNotFoundError
from errors.error_dsi import DeveloperSkillIssue
from flag import Flag

# pylint: disable=line-too-long


class TestTail(unittest.TestCase):
    """
    A test class for the Tail class.
    """

    def setUp(self) -> None:
        self.in_stream = StringIO()
        self.out_stream = StringIO()
        self.mock_file = mock_open(
            read_data="line1\nline2\nline3\nline4\nline5\nline6\nline7\nline8\nline9\nline10\n"  # noqa
        )

    def tearDown(self) -> None:
        self.in_stream.close()
        self.out_stream.close()

    @parameterized.expand(
        [
            (
                [Flag("n", 5, "For testing")],
                None,
                "line6\nline7\nline8\nline9\nline10\n",
            ),
            (
                [],
                None,
                "line1\nline2\nline3\nline4\nline5\nline6\nline7\nline8\nline9\nline10\n",  # noqa
            ),
            (
                [Flag("n", -3, "For testing")],
                None,
                "line8\nline9\nline10\n",
            ),
            (
                [Flag("n", -100, "For testing")],
                None,
                "line1\nline2\nline3\nline4\nline5\nline6\nline7\nline8\nline9\nline10\n",  # noqa
            ),
            (
                [Flag("n", 0, "For testing")],
                None,
                "",
            ),
            (
                [],
                "line1\nline2\nline3\nline4\nline5\nline6\nline7\nline8\nline9\nline10\n",  # noqa
                "line1\nline2\nline3\nline4\nline5\nline6\nline7\nline8\nline9\nline10\n",  # noqa
            ),
            (
                [Flag("n", 5, "For testing")],
                "line1\nline2\nline3\nline4\nline5\nline6\nline7\nline8\nline9\nline10\n",  # noqa
                "line6\nline7\nline8\nline9\nline10\n",
            ),
        ]
    )
    def test_tail_parameterised(
        self,
        flags: List[Flag],
        stdin: Optional[str],
        expected_output: Optional[str],
    ) -> None:
        """
        Uses parameterised expand to test the tail command with different
        parameters
        """
        with patch("builtins.open", self.mock_file):
            if stdin is not None:
                self.in_stream.write(stdin)
                self.in_stream.seek(0)
                tail = Tail(self.in_stream, self.out_stream, flags, [])
                tail.run()
                self.assertEqual(tail.output.getvalue(), expected_output)
            else:
                tail = Tail(self.in_stream, self.out_stream, flags, ["file1"])
                tail.run()
                self.assertEqual(tail.output.getvalue(), expected_output)

    @parameterized.expand(
        [
            (
                [Flag("n", [1, 3, 4], "For testing")],
                DeveloperSkillIssue,
            ),
            (
                [Flag("a", 10, "For testing")],
                DeveloperSkillIssue,
            ),
        ]
    )
    def test_tail_exceptions(
        self,
        flags: List[Flag],
        expected_exception: Type[Exception],
    ) -> None:
        """
        Uses parameterised expand to test the tail command with different
        exceptions
        """
        with patch("builtins.open", self.mock_file):
            with self.assertRaises(expected_exception):
                tail = Tail(self.in_stream, self.out_stream, flags, ["file1"])
                tail.run()

    def test_tail_too_many_files(self) -> None:
        """
        Tests the tail command with too many files
        """
        flags: List[Flag] = []
        options = ["file1", "file2"]
        with self.assertRaises(CommandError):
            Tail(self.in_stream, self.out_stream, flags, options).run()

    def test_tail_no_file(self) -> None:
        """
        Tests the tail command with no file
        """
        flags: List[Flag] = []
        options: List[str] = []
        with self.assertRaises(CommandError):
            Tail(self.in_stream, self.out_stream, flags, options).run()

    def test_tail_full_too_many_files(self) -> None:
        """
        Tests the tail command by mocking read_lines_from_file and more than
        one file
        """
        filenames = ["mock_file.txt", "mock_file2.txt"]
        flags: List[Flag] = []
        with patch("builtins.open", filenames):
            with self.assertRaises(CommandError):
                tail = Tail(self.in_stream, self.out_stream, flags, filenames)
                tail.run()

    def test_tail_full_nonexistant_file(self) -> None:
        """
        Tests the tail command by mocking read_lines_from_file and no flag
        """
        filename = "mock_file.txt"
        flags: List[Flag] = []
        with self.assertRaises(ShellFileNotFoundError):
            tail = Tail(self.in_stream, self.out_stream, flags, [filename])
            tail.run()

    def test_tail_permission_error(self) -> None:
        """
        Tests the tail command by mocking open raising permission error
        """
        filename = "mock_file.txt"
        flags: List[Flag] = []
        with patch("builtins.open", side_effect=PermissionError):
            with self.assertRaises(CommandError):
                tail = Tail(self.in_stream, self.out_stream, flags, [filename])
                tail.run()

    def test_tail_os_error(self) -> None:
        """
        Tests the tail command by mocking open raising os error
        """
        filename = "mock_file.txt"
        flags: List[Flag] = []
        with patch("builtins.open", side_effect=OSError):
            with self.assertRaises(CommandError):
                tail = Tail(self.in_stream, self.out_stream, flags, [filename])
                tail.run()


if __name__ == "__main__":
    unittest.main()
