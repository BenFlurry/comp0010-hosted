"""
Module for testing the sort module.
"""
import unittest
from io import StringIO
from typing import List, Optional, Type
from unittest.mock import mock_open, patch

from parameterized import parameterized

from commands.sortcommand import Sort
from errors.command_errors import CommandError, ShellFileNotFoundError
from errors.error_dsi import DeveloperSkillIssue
from flag import FlagSpecification, FlagValue


class TestSort(unittest.TestCase):
    """
    Test class for the sort command.
    """

    def setUp(self) -> None:
        """
        Sets up the test class.
        """
        self.in_stream = StringIO()
        self.out_stream = StringIO()
        self.mock_file = mock_open(read_data="c\na\nb\n2\n1\n3\n")
        self.r_flag = FlagSpecification(
            "r", bool, "test flag"
        ).build_flag_with_value(True)
        self.wrong_flag = FlagSpecification(
            "w", bool, "wrong flag"
        ).build_flag_with_value(True)
        self.test_files = ["test1.txt", "test2.txt", "test3.txt"]

    def tearDown(self) -> None:
        """
        Tears down the test class.
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
        with patch("os.path.exists", return_value=True):
            with patch("builtins.open", self.mock_file):
                sort = Sort(self.in_stream, self.out_stream, flags, options)
                sort.run()
                self.assertEqual(self.out_stream.getvalue(), expected_output)

    @parameterized.expand(
        [
            ("", [], ["test1.txt"], "1\n2\n3\na\nb\nc\n"),  # test_sort_basic
            (
                "",
                [
                    FlagSpecification(
                        "r", bool, "test flag"
                    ).build_flag_with_value(True)
                ],
                ["test1.txt"],
                "c\nb\na\n3\n2\n1\n",
            ),  # test_sort_reverse
            (
                "",
                [
                    FlagSpecification(
                        "w", bool, "wrong flag"
                    ).build_flag_with_value(True)
                ],
                [],
                "",
                DeveloperSkillIssue,
            ),  # test_sort_wrong_flag
            (
                "3\n2\n1\na\nb\nc\n",
                [],
                [],
                "1\n2\n3\na\nb\nc\n",
            ),  # test_sort_stdin
            (
                "3\n2\n1\na\nb\nc\n",
                [
                    FlagSpecification(
                        "r", bool, "test flag"
                    ).build_flag_with_value(True)
                ],
                [],
                "c\nb\na\n3\n2\n1\n",
            ),  # test_sort_reverse_stdin
            (
                "",
                [],
                [],
                "",
                CommandError,
            ),  # test_sort_no_option_or_stdin
            (
                "",
                [
                    FlagSpecification(
                        "r", bool, "test flag"
                    ).build_flag_with_value(True),
                    FlagSpecification(
                        "r", bool, "test flag"
                    ).build_flag_with_value(True),
                ],
                [],
                "",
                CommandError,
            ),  # test_sort_too_many_flags
            (
                "",
                [],
                ["test1.txt", "test2.txt"],
                "",
                CommandError,
            ),  # test_sort_too_many_options
        ]
    )
    def test_sort_variations(  # pylint: disable=too-many-arguments
        self,
        stdin: str,
        flags: List[FlagValue],
        options: List[str],
        expected_output: str,
        expected_exception: Optional[Type[Exception]] = None,
    ) -> None:
        """
        Test sort command with various options and flags.
        """
        if stdin:
            self.in_stream.write(stdin)

        if expected_exception:
            with self.assertRaises(expected_exception):
                self._open_helper(flags, options, expected_output)
        else:
            self._open_helper(flags, options, expected_output)

    def test_sort_permissions_errors(self) -> None:
        """
        Tests sort with a file that has permission errors.
        """
        with patch("os.path.exists", return_value=True):
            with patch("builtins.open", side_effect=PermissionError()):
                with self.assertRaises(CommandError):
                    sort = Sort(
                        self.in_stream,
                        self.out_stream,
                        [],
                        [self.test_files[0]],
                    )
                    sort.run()

    def test_sort_os_errors(self) -> None:
        """
        Tests sort with a file that has os errors.
        """
        with patch("os.path.exists", return_value=True):
            with patch("builtins.open", side_effect=OSError()):
                with self.assertRaises(CommandError):
                    sort = Sort(
                        self.in_stream,
                        self.out_stream,
                        [],
                        [self.test_files[0]],
                    )
                    sort.run()

    def test_sort_file_not_found(self) -> None:
        """
        Tests sort with a file that does not exist.
        """
        with patch("os.path.exists", return_value=False):
            with self.assertRaises(ShellFileNotFoundError):
                sort = Sort(
                    self.in_stream, self.out_stream, [], [self.test_files[0]]
                )
                sort.run()


if __name__ == "__main__":
    unittest.main()
