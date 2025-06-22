"""
Tests the Seq runnable
"""

import unittest
from io import StringIO
from unittest import mock

from commands.base_command import BaseCommand
from commands.seq import Seq


class TestSeq(unittest.TestCase):
    """
    A test class for the Seq runnable
    """

    def setUp(self) -> None:
        """
        The setup function from unittest.TestCase, called every time a test is
        ran. here we use mock.create_autospec to auto mock the runnable class
        """
        self.runnable = mock.create_autospec(BaseCommand)
        self.runnable.out_stream = StringIO()
        self.runnable.in_stream = StringIO()
        self.runnable.run.return_value = 0
        self.in_stream = StringIO()
        self.out_stream = StringIO()
        self.seq = Seq(self.runnable, self.runnable)

    def test_seq_normal(self) -> None:
        """
        a normal test for the seq command
        """
        self.assertEqual(self.seq.run(), 0)

    def test_seq_close(self) -> None:
        """
        a test to ensure seq's output closes when close() is ran
        """
        self.seq.close()
        self.runnable.close.assert_called_with()

    def test_seq_output_stream(self) -> None:
        """
        A test to ensure that 2 different commands have their output streams
        correctly merged by the seq command
        """
        left = mock.create_autospec(BaseCommand)
        right = mock.create_autospec(BaseCommand)
        left.out_stream = StringIO()
        right.out_stream = left.out_stream
        left.out_stream.write("hello")
        right.out_stream.write("hi")
        Seq(left, right).run()
        self.assertEqual(right.out_stream.getvalue(), "hellohi")
