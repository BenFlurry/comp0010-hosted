"""
Test the pipe builder
"""
import unittest
from io import StringIO
from typing import Optional
from unittest import mock

from commands.builder import Builder
from commands.pipe import Pipe
from commands.pipe_builder import PipeBuilder
from errors.error_dsi import DeveloperSkillIssue


class TestPipeBuilder(unittest.TestCase):
    """
    Tests the pipe builder
    """

    def setUp(self):
        self.left = mock.create_autospec(Builder)
        self.right = mock.create_autospec(Builder)
        self.in_stream = StringIO()
        self.out_stream = StringIO()

    def tearDown(self) -> None:
        if self.in_stream:
            self.in_stream.close()
        if self.out_stream:
            self.out_stream.close()

    def _pipe_builder_helper(
        self, in_stream: Optional[StringIO], out_stream: Optional[StringIO]
    ):
        pipe_builder = PipeBuilder(self.left, self.right)
        pipe_builder.set_in_stream(in_stream)
        pipe_builder.set_out_stream(out_stream)

        return pipe_builder.build()

    def test_pipe_builder_normal(self):
        """
        Test the pipe builder in the normal case
        """
        pipe = self._pipe_builder_helper(self.in_stream, self.out_stream)
        self.assertIsInstance(pipe, Pipe)

    def test_pipe_builder_no_left(self):
        """
        Test the pipe builder when there is no left builder
        """
        self.left = None
        with self.assertRaises(DeveloperSkillIssue):
            self._pipe_builder_helper(self.in_stream, self.out_stream)

    def test_pipe_builder_no_right(self):
        """
        Test the pipe builder when there is no right builder
        """
        self.right = None
        with self.assertRaises(DeveloperSkillIssue):
            self._pipe_builder_helper(self.in_stream, self.out_stream)

    def test_pipe_left_pipe(self):
        """
        Test the pipe builder when the left command is a pipe
        """
        self.left = PipeBuilder(self.left, self.right)
        pipe = self._pipe_builder_helper(self.in_stream, self.out_stream)
        self.assertIsInstance(pipe, Pipe)


if __name__ == "__main__":
    unittest.main()
