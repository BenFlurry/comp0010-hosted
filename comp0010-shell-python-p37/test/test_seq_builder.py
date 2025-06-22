"""
Tests seq builder
"""

import unittest
from io import StringIO
from typing import Optional
from unittest.mock import create_autospec

from commands.builder import Builder
from commands.runnable import Runnable
from commands.seq import Seq
from commands.seq_builder import SeqBuilder


class TestSeqBuilder(unittest.TestCase):
    """
    Tests the seq builder checking
    """

    def setUp(self) -> None:
        self.left_builder = create_autospec(Builder)
        self.right_builder = create_autospec(Builder)
        self.in_stream = StringIO()
        self.out_stream = StringIO()

    def tearDown(self) -> None:
        self.in_stream.close()
        self.out_stream.close()

    def _seq_builder_helper(self,
                            in_stream: Optional[StringIO],
                            out_stream: Optional[StringIO]) -> Runnable:
        """
        a helper function to set the in and out stream for seq builder, and
        build the function using the mock
        """
        seq_builder = SeqBuilder(self.left_builder, self.right_builder)

        if in_stream:
            seq_builder.set_in_stream(in_stream)

        if out_stream:
            seq_builder.set_out_stream(out_stream)

        return seq_builder.build()

    def test_seq_builder_normal(self) -> None:
        """
        A normal test for seq builder, where the input stream is given
        """
        self.in_stream.write("some in stream")
        self.out_stream.write("some out stream")
        seq = self._seq_builder_helper(self.in_stream, self.out_stream)
        self.assertIsInstance(seq, Seq)
