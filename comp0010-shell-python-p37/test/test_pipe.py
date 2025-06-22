"""
Module to test pipes
"""

import unittest
from io import StringIO
from unittest import mock

from commands.base_command import BaseCommand
from commands.pipe import Pipe


class TestPipe(unittest.TestCase):
    """
    Tests the pipe
    """

    def setUp(self):
        self.in_stream = StringIO()
        self.mid_stream = StringIO()
        self.out_stream = StringIO()
        self.runnable1 = mock.create_autospec(BaseCommand)
        self.runnable1.out_stream = self.mid_stream
        self.runnable1.in_stream = StringIO()
        self.runnable1.run.return_value = 0
        self.runnable2 = mock.create_autospec(BaseCommand)
        self.runnable2.out_stream = StringIO()
        self.runnable2.in_stream = self.mid_stream
        self.runnable2.run.return_value = 0

        self.pipe = Pipe(self.runnable1, self.runnable2, self.mid_stream)

    def tearDown(self) -> None:
        self.in_stream.close()
        self.out_stream.close()

    def test_pipe_normal(self):
        """
        Test the pipe builder in the normal case
        """
        self.assertEqual(self.pipe.run(), 0)

    def test_pipe_in_pipe(self):
        """
        Test the pipe builder in the case where the left command is a pipe
        """
        self.pipe.left = Pipe(self.runnable1, self.runnable2, self.mid_stream)
        self.assertEqual(self.pipe.run(), 0)

    def test_pipe_close(self):
        """
        Test that the pipe builder closes the streams
        """
        self.pipe.close()
        self.runnable1.close.assert_called_with()
        self.runnable2.close.assert_called_with()

    def test_pipe_midstream(self):
        """
        Test to ensure the midstream is correctly seeked to the start
        """
        self.pipe.left.out_stream.write("test")
        self.assertEqual(self.pipe.left.out_stream.read(), "")
        self.pipe.run()
        self.assertEqual(self.pipe.left.out_stream.read(), "test")


if __name__ == "__main__":
    unittest.main()
