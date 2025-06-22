"""
Module to test the sed command
"""
import unittest
from io import StringIO
from typing import List, Optional, Type
from unittest.mock import _patch, mock_open, patch

from parameterized import parameterized

from commands.sedcommand import Sed
from errors.command_errors import CommandError


class TestSed(unittest.TestCase):
    """
    Class to test the grep command
    """
    def setUp(self) -> None:
        self.patched: Optional[_patch] = None

    def tearDown(self):
        if self.patched is not None:
            self.patched.stop()

    def _make_sed(self,
                  expression: str,
                  std_content: Optional[str],
                  file_content: Optional[str]):
        in_stream = StringIO()
        out_stream = StringIO()
        options: List[str] = [expression]
        if std_content is not None:
            in_stream.write(std_content)
            in_stream.seek(0)

        if file_content is not None:
            self.patched = patch('builtins.open',
                                 mock_open(read_data=file_content))
            self.patched.start()
            options.append('file.txt')

        return Sed(in_stream, out_stream, [], options)

    @parameterized.expand({
        ("s/A/C/", None, "AAA\nBBB\nAAA", "CAA\nBBB\nCAA"),
        ("s/A/C/g", None, "CCC\nBBB\nCCC", "CCC\nBBB\nCCC"),
        ("s|A|C|", None, "AAA\nBBB\nAAA", "CAA\nBBB\nCAA"),
        ("s|A|C|g", None, "CCC\nBBB\nCCC", "CCC\nBBB\nCCC"),
        ("s/A/C/", "AAA\nBBB\nAAA", None, "CAA\nBBB\nCAA"),
        ("s/A/C/g", "CCC\nBBB\nCCC", None, "CCC\nBBB\nCCC"),
        ("s/../CC/", "AAA\nBBB\nAAA", None, "CCA\nCCB\nCCA"),
    })
    def test_sed_happy(self,
                       expression: str,
                       std_content: Optional[str],
                       file_content: Optional[str],
                       expected_output: str) -> None:
        """
        Tests the sed command when it is happy
        """
        with self._make_sed(expression, std_content, file_content) as sed:
            sed.run()
            self.assertEqual(sed.output.getvalue(), expected_output)

    # pylint: disable=too-many-arguments
    @parameterized.expand({
        ("s/A/C", None, "AAA\nBBB\nAAA", CommandError, 'Invalid expression'),
        ("s|A|C", None, "CCC\nBBB\nCCC", CommandError, 'Invalid expression'),
        ("s%", None, "AAA\nBBB\nAAA", CommandError, 'sed prefix'),
        ("s|[1|C|g", None, "CCC\nBBB\nCCC", CommandError, 'Invalid pattern'),
    })
    def test_sed_sad(self,
                     expression: str,
                     std_content: Optional[str],
                     file_content: Optional[str],
                     expected_exception_cls: Type[BaseException],
                     expected_message: str) -> None:
        """
        Tests the sed command when it is (very) sad
        """
        with self.assertRaisesRegex(expected_exception_cls, expected_message):
            with self._make_sed(expression, std_content, file_content) as sed:
                sed.run()

    def test_sed_no_options(self):
        """
        Sed with no options
        """
        with self.assertRaisesRegex(CommandError, 'Not enough arguments'):
            Sed(StringIO(), StringIO(), [], [])

    def test_sed_no_file_no_stdin(self):
        """
        Sed with no file and no stdin
        """
        with self.assertRaisesRegex(CommandError, 'No input provided'):
            Sed(StringIO(), StringIO(), [], ['s/something/another/g']).run()


if __name__ == "__main__":
    unittest.main()
