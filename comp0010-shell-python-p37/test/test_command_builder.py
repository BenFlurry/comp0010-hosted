"""
Tests command builder
"""

import unittest
from io import StringIO
from typing import List, Optional

from commands.base_command import BaseCommand
from commands.command_builder import CommandBuilder
from flag import Flag, FlagSpecification


# pylint: disable=too-few-public-methods
class MockCommand(BaseCommand):
    """
    A command inheriting from BaseCommand, but mocked.
    """
    _acceptable_flags: List[FlagSpecification] = []
    command_name: str = 'mock'
    command_help_text = ('irrelavent', 'here')

    def run(self) -> int:
        """
        Mocked run method
        """
        raise NotImplementedError()


class TestCommandBuilder(unittest.TestCase):
    """
    Tests that the command builder passes the right stuff to the command when
    it is being built
    """
    def make_cmd_builder_with(self,
                              in_stream: Optional[StringIO],
                              out_stream: Optional[StringIO]):
        """
        Creates a command builder with the given input and output streams.

        Args:
            in_stream (Optional[StringIO]): The input stream to build with
            out_stream (Optional[StringIO]): The output stream to build with
        """
        cmd_builder = CommandBuilder(MockCommand)
        if in_stream is not None:
            cmd_builder.set_in_stream(in_stream)

        if out_stream is not None:
            cmd_builder.set_out_stream(out_stream)

        return cmd_builder

    def test_happy_command_builder(self):
        """
        Ensures that in the normal case, a command builder indeed builds a mock
        command
        """
        cmd_builder = self.make_cmd_builder_with(StringIO(), StringIO())
        self.assertIsInstance(cmd_builder.build(), MockCommand)

    def test_happy_command_builder_with_flags(self):
        """
        Ensures that in the normal case, a command builder indeed builds a mock
        command with flags
        """
        cmd_builder = self.make_cmd_builder_with(StringIO(), StringIO())
        flag = Flag[int]('t', 100, 'some flag')
        cmd = cmd_builder.add_flag(flag).build()
        self.assertIsInstance(cmd, MockCommand)
        self.assertIn(flag, cmd.flags)

    def test_happy_command_builder_with_options(self):
        """
        Ensures that in the normal case, a command builder indeed builds a mock
        command with options
        """
        cmd_builder = self.make_cmd_builder_with(StringIO(), StringIO())
        option = 'hello'
        cmd = cmd_builder.add_option(option).build()
        self.assertIsInstance(cmd, MockCommand)
        self.assertIn(option, cmd.options)

    def test_happy_command_builder_with_chain(self):
        """
        Ensures that in the normal case, a command builder's functions can be
        chained
        """
        cmd_builder = self.make_cmd_builder_with(StringIO(), StringIO())
        option_1 = 'hi'
        option_2 = 'world'
        flag_1 = Flag[int]('r', 100, 'a flag')
        flag_2 = Flag[str]('e', 'yes', 'another flag')
        cmd = cmd_builder \
            .add_option(option_1) \
            .add_option(option_2) \
            .add_flag(flag_1) \
            .add_flag(flag_2) \
            .build()
        self.assertIsInstance(cmd, MockCommand)
        self.assertEqual([option_1, option_2], cmd.options)
        self.assertIn(flag_1, cmd.flags)
        self.assertIn(flag_2, cmd.flags)


if __name__ == '__main__':
    unittest.main()
