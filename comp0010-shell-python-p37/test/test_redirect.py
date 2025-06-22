"""
Tests the Redirect runnable
"""
import unittest
from io import StringIO
from unittest.mock import MagicMock

from parameterized import parameterized

from commands.redirect import Redirect
from errors.error_dsi import DeveloperSkillIssue


class TestRedirect(unittest.TestCase):
    """
    A test class for the Redirect runnable.

    The Redirect runnable should have the following specificaitons:
    1. All inputs to in_stream should go into the wrapped object
    2. All outputs from the wrapped object should go into out_stream

    Redirect expects the builder to expose the wrapped streams, so we don't
    have to dig too deep into the runnable to figure out if their in_stream /
    out_stream has been called.
    """
    def setUp(self) -> None:
        self.in_stream = StringIO()
        self.out_stream = StringIO()
        self.wrapped_in_stream = StringIO()
        self.wrapped_out_stream = StringIO()

        self.runnable = MagicMock()
        self.redirect = Redirect(
            self.in_stream,
            self.out_stream,
            self.wrapped_in_stream,
            self.wrapped_out_stream,
            self.runnable
        )

    def test_happy_spec_input(self):
        """
        Tests that all input goes into the command
        """
        self.in_stream.write('for testing')
        self.in_stream.seek(0)
        with self.redirect:
            self.redirect.run()
            self.runnable.run.assert_called_once()
            self.assertEqual(self.wrapped_in_stream.getvalue(), 'for testing')

    def test_happy_spec_output(self):
        """
        Tests that all output goes from the command to our out_stream
        """
        self.runnable.run = MagicMock(
            wraps=lambda: self.wrapped_out_stream.write('hi'))

        with self.redirect:
            self.redirect.run()
            self.runnable.run.assert_called_once()
            self.assertEqual(self.out_stream.getvalue(), 'hi')

    @parameterized.expand({
        (True, 0, 100, False),
        (False, 0, 100, True),
        (True, 0, 0, True)
    })
    def test_stream_is_empty(self,
                             seekable: bool,
                             curr_pos: int,
                             final_pos: int,
                             expected_ret_val: bool):
        """
        Checks if the function stream_is_empty returns the right values
        """
        stream = MagicMock()

        def mock_tell():
            count = stream.tell.call_count
            if count == 1:
                return curr_pos

            if count == 2:
                return final_pos
            raise RuntimeError('unexpected call')

        stream.seekable = MagicMock(return_value=seekable)
        stream.tell = MagicMock(side_effect=mock_tell)
        self.assertEqual(
            self.redirect.stream_is_empty(stream), expected_ret_val)

    def test_closed(self):
        """
        If the redirect is closed, an DeveloperSkillIssue should occur
        """
        self.redirect.close()
        with self.assertRaises(DeveloperSkillIssue):
            self.redirect.run()


if __name__ == '__main__':
    unittest.main()
