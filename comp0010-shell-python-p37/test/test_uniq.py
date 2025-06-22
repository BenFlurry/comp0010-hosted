"""
Module to test the uniq module.
"""
import unittest
from io import StringIO
from typing import List
from unittest.mock import mock_open, patch

from parameterized import parameterized

from commands.uniqcommand import Uniq
from errors.command_errors import CommandError, ShellFileNotFoundError
from errors.error_dsi import DeveloperSkillIssue
from flag import FlagSpecification, FlagValue


class TestUniq(unittest.TestCase):
    """
    Tests the uniq command class
    """

    def setUp(self):
        """
        Set up the uniq command for testing
        """
        self.in_stream = StringIO()
        self.out_stream = StringIO()

    def tearDown(self):
        """
        Close the streams
        """
        self.in_stream.close()
        self.out_stream.close()

    def _open_helper(
        self,
        flags: List[FlagValue],
        options: List[str],
        read_data: str,
        expected_output: str,
    ) -> None:
        """
        Helper function to open a file
        """
        mock_file = mock_open(read_data=read_data)
        with patch("builtins.open", mock_file), patch(
            "os.path.exists", return_value=True
        ):
            uniq = Uniq(self.in_stream, self.out_stream, flags, options)
            uniq.run()
            self.assertEqual(self.out_stream.getvalue(), expected_output)

    @parameterized.expand(
        [
            [
                [],
                ["test_file"],
                "line1\nline2\nline2\nLine2\nline5\nline2",
                "line1\nline2\nLine2\nline5\nline2\n",
                None,
                None,
            ],
            [
                [
                    FlagSpecification(
                        "i", bool, "test flag"
                    ).build_flag_with_value(True)
                ],
                ["test_file"],
                "line1\nline2\nline2\nLine2\nline5\nline2",
                "line1\nline2\nline5\nline2\n",
                None,
                None,
            ],
            [
                [
                    FlagSpecification(
                        "i", bool, "test flag"
                    ).build_flag_with_value(True),
                    FlagSpecification(
                        "b", bool, "test flag"
                    ).build_flag_with_value(True),
                ],
                ["test_file"],
                "line1\nline2\nline2\nLine2\nline5\nline2",
                "error",
                None,
                CommandError,
            ],
            [
                [
                    FlagSpecification(
                        "b", bool, "test flag"
                    ).build_flag_with_value(True)
                ],
                ["test_file"],
                "line1\nline2\nline2\nLine2\nline5\nline2",
                "error",
                None,
                DeveloperSkillIssue,
            ],
            [
                [],
                ["test_file1", "test_file2"],
                "line1\nline2\nline2\nLine2\nline5\nline2",
                "error",
                None,
                CommandError,
            ],
            [
                [
                    FlagSpecification(
                        "i", bool, "test flag"
                    ).build_flag_with_value(True)
                ],
                [],
                None,
                "line1\nline2\nline5\nline2\n",
                "line1\nline2\nline2\nLine2\nline5\nline5\nline2",
                None,
            ],
            [
                [
                    FlagSpecification(
                        "i", bool, "test flag"
                    ).build_flag_with_value(True)
                ],
                [],
                "",
                "error",
                None,
                CommandError,
            ],
            [
                [],
                ["test_file"],
                "AAA\naaa\nAAA",
                "AAA\naaa\nAAA\n",
                None,
                None,
            ],
            [
                [
                    FlagSpecification(
                        "i", bool, "test flag"
                    ).build_flag_with_value(True)
                ],
                ["test_file"],
                "AAA\naaa\nAAA",
                "AAA\n",
                None,
                None,
            ],
        ]
    )
    def test_uniq_param(  # pylint: disable=too-many-arguments
        self, flags, options, read_data, expected_output, stdin, exception
    ) -> None:
        """
        Tests the uniq command using parameterized testing
        """
        if stdin is not None:
            self.in_stream.write(stdin)
            self.in_stream.seek(0)
        if exception is not None:
            with self.assertRaises(exception):
                self._open_helper(flags, options, read_data, expected_output)
        else:
            self._open_helper(flags, options, read_data, expected_output)

    @parameterized.expand(
        [
            [
                "builtins.open",
                FileNotFoundError,
                ShellFileNotFoundError,
            ],
            [
                "builtins.open",
                PermissionError,
                CommandError,
            ],
        ]
    )
    def test_uniq_exceptions(
        self, exception_source, exception, expected_exception
    ) -> None:
        """
        Tests the uniq command for exceptions
        """
        with self.assertRaises(expected_exception), patch(
            f"{exception_source}", side_effect=exception
        ):
            uniq = Uniq(self.in_stream, self.out_stream, [], ["test_file"])
            uniq.run()


if __name__ == "__main__":
    unittest.main()
