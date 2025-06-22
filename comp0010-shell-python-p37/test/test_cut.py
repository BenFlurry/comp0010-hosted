"""
This module tests the cut command
"""
import unittest
from io import StringIO, TextIOBase
from typing import List, Optional, Tuple, Type
from unittest.mock import MagicMock, mock_open, patch

from parameterized import parameterized

from commands.cutcommand import Cut
from errors.command_errors import (CommandError, UnknownFlagError,
                                   UnknownFlagValueError)
from flag import FlagSpecification


class TestCut(unittest.TestCase):
    """
    Tests the cut command and any helper functions
    """
    def build_cut(self, in_stream: Optional[TextIOBase],
                  out_stream: Optional[TextIOBase],
                  range_str: str) -> Cut:
        """
        Builds a cut command.
        """
        return Cut(StringIO() if in_stream is None else in_stream,
                   StringIO() if out_stream is None else out_stream,
                   [FlagSpecification('b', List[str], '')
                    .build_flag_from_string(range_str)], ['file.txt'])

    @parameterized.expand({
        ('1', 999, (1, 1)),
        ('1-5', 999, (1, 5)),
        ('-5', 999, (1, 5)),
        ('5-', 10, (5, 10)),
        ('1-1000', 999, (1, 999))
    })
    def test_good_start_end_range(self,
                                  input_str: str,
                                  max_num: int,
                                  expected_output: Tuple[int]):
        """
        Tests the good_start_end_range returns the correct ranges

        Arguments:
            input_str (str): The input string to parse.
            max_num (int): The maximum number to be returned by the range, if
                           required
            expected_output (Tuple[int]): This is supposed to be a list, but
                                          parameterized.expand doesn't like
                                          lists because they are not hashable,
                                          so we're using a tuple instead
        """
        cut = self.build_cut(None, None, input_str)
        self.assertEqual(
            list(cut.get_start_to_end_from_str(
                input_str, max_num)), list(expected_output))

    @parameterized.expand({
        ('--1', 999, CommandError, 'maximally one'),
        ('1--', 999, CommandError, 'maximally one'),
        ('a-b', 999, CommandError, 'unknown'),
        ('a', 999, CommandError, 'to int'),
        ('-b', 999, CommandError, 'unknown'),
        ('5-1', 999, CommandError, 'decreasing'),
        ('0', 999, CommandError, 'byte positions'),
        ('0-123', 999, CommandError, 'byte positions'),
        ('', 999, UnknownFlagValueError, 'option requires an argument')
    })
    def test_bad_start_end_range(self,
                                 input_str: str,
                                 max_num: int,
                                 expected_error: Type[BaseException],
                                 expected_regex: str):
        """
        Tests the bas_start_end_range throws exceptions

        Arguments:
            input_str (str): The input string to parse.
            max_num (int): The maximum number to be returned by the range, if
                           required
            expected_error (Type[BaseException]): The expected class of error
                                                  thrown
            expected_regex (str): A string expected within the exception
        """
        cut = self.build_cut(None, None, '1')
        with self.assertRaisesRegex(expected_error, expected_regex):
            cut.get_start_to_end_from_str(
                input_str, max_num
            )

    @parameterized.expand([
        ([(1, 3), (3, 4)], [(1, 4)]),
        ([(1, 10), (2, 9)], [(1, 10)]),
        ([(1, 3), (2, 4)], [(1, 4)]),
        ([], []),
        ([(1, 10)], [(1, 10)]),
        ([(1, 3), (6, 10), (2, 4)], [(1, 4), (6, 10)]),
        ([(1, 3), (5, 10), (2, 4)], [(1, 4), (5, 10)]),
    ])
    def test_unionized_iterator(self,
                                input_data: List[Tuple[int, int]],
                                expected_output: List[Tuple[int, int]]):
        """
        Tests the unionized iterator

        Arguments:
            input_str (List[Tuple[int, int]]): The input data to parse.
            expected_output (List[Tuple[int, int]]): This is supposed to be a
                                                     list, but
                                                     parameterized.expand
                                                     doesn't like lists because
                                                     they are not hashable, so
                                                     we're using a tuple
                                                     instead
        """
        self.assertEqual(list(Cut.unionized_iterator(MagicMock(),
                                                     iter(input_data))),
                         expected_output)

    @parameterized.expand({
        ('1-3', 'ohayo\nsekai', 'oha\nsek'),
        ('1-3', '', ''),
        ('1-3,5-8',
         "the pain won't go away\nhelp me please",
         'thepain\nhel me '),
        ('1-4,11-',
         "they said i was crazy\nistg i hear voices every night",
         "theyi was crazy\nistgr voices every night"),
        ('-2,-3',
         "no game no life zero is a masterpiece",
         "no ")
    })
    def test_cut_happy(self,
                       range_str: str,
                       file_content: str,
                       expected_output: str):
        """
        Tests happy cases of cut

        Arguments:
            range_str (str): A string to parse
            file_content (str): The contents of the file
            expected_output (str): The expected output of the cut command
        """
        input_stream, output_stream = StringIO(), StringIO()
        cut = self.build_cut(input_stream, output_stream, range_str)
        with patch('builtins.open', mock_open(read_data=file_content)):
            self.assertEqual(cut.run(), 0)
            self.assertEqual(output_stream.getvalue(), expected_output)

    def test_stdin(self):
        """
        Tests reading from stdin. All other code is the same, so we don't
        bother testing multiple inputs
        """
        input_stream, output_stream = StringIO(), StringIO()
        input_stream.write('ohayo\nsekai')
        input_stream.seek(0)
        cut = Cut(input_stream, output_stream, [
            FlagSpecification('b', List[str], '')
            .build_flag_from_string('1-3')
        ], [])
        self.assertEqual(cut.run(), 0)
        self.assertEqual(output_stream.getvalue(), 'oha\nsek')

    @parameterized.expand({(0,), (2,)})
    def test_cut_sad_flags(self, no_flags: int):
        """
        It is already guaranteed that the parser will discard non-related
        flags, so we only have to check for number of flags.

        Cut in bash also only accepts exactly one list

        Arguments:
            no_flags (int): Number of flags to pass to cut.
        """
        flag = FlagSpecification('b', List[str], '') \
            .build_flag_from_string('1-3')
        input_stream = StringIO()
        input_stream.write('does not matter')
        input_stream.seek(0)
        with self.assertRaises(UnknownFlagError):
            Cut(input_stream, StringIO(), [flag] * no_flags, [])

    def test_no_stdin_no_file(self):
        """
        If both stdin and file are empty, cut should throw an exception
        """
        with self.assertRaisesRegex(CommandError, 'no file provided'):
            Cut(StringIO(), StringIO(),
                [FlagSpecification('b', List[str], '')
                .build_flag_from_string('')], []).run()


if __name__ == '__main__':
    unittest.main()
