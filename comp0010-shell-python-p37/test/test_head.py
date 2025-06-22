"""
A module that contains unit tests for the echo command.
"""
import unittest
from io import StringIO
from unittest.mock import mock_open, patch
from typing import List, Optional, Type

from parameterized import parameterized

from commands.headcommand import Head
from errors.command_errors import CommandError, ShellFileNotFoundError
from errors.error_dsi import DeveloperSkillIssue
from flag import Flag

# pylint: disable=line-too-long


class TestHead(unittest.TestCase):
    """
    A test class for the Head class.
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
                "line1\nline2\nline3\nline4\nline5\n",
            ),
            (
                [],
                None,
                "line1\nline2\nline3\nline4\nline5\nline6\nline7\nline8\nline9\nline10\n",  # noqa
            ),
            (
                [Flag("n", -3, "For testing")],
                None,
                "line1\nline2\nline3\nline4\nline5\nline6\nline7\n",
            ),
            (
                [Flag("n", -100, "For testing")],
                None,
                "",
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
                "line1\nline2\nline3\nline4\nline5\n",
            ),
        ]
    )
    def test_head_parameterised(
        self,
        flags: List[Flag],
        stdin: Optional[str],
        expected_output: Optional[str],
    ) -> None:
        """
        Uses parameterised expand to test the head command with different
        parameters
        """
        with patch("builtins.open", self.mock_file):
            if stdin is not None:
                self.in_stream.write(stdin)
                self.in_stream.seek(0)
                head = Head(self.in_stream, self.out_stream, flags, [])
                head.run()
                self.assertEqual(head.output.getvalue(), expected_output)
            else:
                head = Head(self.in_stream, self.out_stream, flags, ["file1"])
                head.run()
                self.assertEqual(head.output.getvalue(), expected_output)

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
    def test_head_exceptions(
        self,
        flags: List[Flag],
        expected_exception: Type[Exception],
    ) -> None:
        """
        Uses parameterised expand to test the head command with different
        exceptions
        """
        with patch("builtins.open", self.mock_file):
            with self.assertRaises(expected_exception):
                head = Head(self.in_stream, self.out_stream, flags, ["file1"])
                head.run()

    def test_head_too_many_files(self) -> None:
        """
        Tests the head command with too many files
        """
        flags: List[Flag] = []
        options = ["file1", "file2"]
        with self.assertRaises(CommandError):
            Head(self.in_stream, self.out_stream, flags, options).run()

    def test_head_no_file(self) -> None:
        """
        Tests the head command with no file
        """
        flags: List[Flag] = []
        options: List[str] = []
        with self.assertRaises(CommandError):
            Head(self.in_stream, self.out_stream, flags, options).run()

    def test_head_full_too_many_files(self) -> None:
        """
        Tests the head command by mocking read_lines_from_file and more than
        one file
        """
        filenames = ["mock_file.txt", "mock_file2.txt"]
        flags: List[Flag] = []
        with patch("builtins.open", filenames):
            with self.assertRaises(CommandError):
                head = Head(self.in_stream, self.out_stream, flags, filenames)
                head.run()

    def test_head_full_nonexistant_file(self) -> None:
        """
        Tests the head command by mocking read_lines_from_file and no flag
        """
        filename = "mock_file.txt"
        flags: List[Flag] = []
        with self.assertRaises(ShellFileNotFoundError):
            head = Head(self.in_stream, self.out_stream, flags, [filename])
            head.run()

    def test_head_permission_error(self) -> None:
        """
        Tests the head command by mocking open raising permission error
        """
        filename = "mock_file.txt"
        flags: List[Flag] = []
        with patch("builtins.open", side_effect=PermissionError):
            with self.assertRaises(CommandError):
                head = Head(self.in_stream, self.out_stream, flags, [filename])
                head.run()

    def test_head_os_error(self) -> None:
        """
        Tests the head command by mocking open raising os error
        """
        filename = "mock_file.txt"
        flags: List[Flag] = []
        with patch("builtins.open", side_effect=OSError):
            with self.assertRaises(CommandError):
                head = Head(self.in_stream, self.out_stream, flags, [filename])
                head.run()


if __name__ == "__main__":
    unittest.main()
