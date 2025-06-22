"""
Tests the base command and how it handles flags
"""

import unittest
from io import StringIO
from unittest import mock

from commands.base_command import BaseCommand
from commands.command_spec import HELP_FLAG, CommandSpecification
from errors.error_dsi import DeveloperSkillIssue
from flag import FlagSpecification


class TestCommandFixture(BaseCommand):
    # pylint: disable=too-few-public-methods
    """
    A basic mock command inheriting from base command.
    """
    COMMAND_SPECIFICATION = CommandSpecification(
        'unit_test_not_relevant', [], ('', '')
    )

    # pylint: disable=missing-function-docstring
    # All subsequent functions are mock functions, which is
    def run(self) -> int:
        return 0


class TestBaseCommand(unittest.TestCase):
    """
    Tests the base command with the mock command fixture
    """

    def setUp(self):
        self.cmd = TestCommandFixture(StringIO(), StringIO(), [], [])

    def assertCommandHelpText(self, text: str, cmd: BaseCommand):
        # This function name is kept this way to conform to assertEqual and
        # assertIn
        # pylint: disable=invalid-name
        """
        Asserts that the text contains command help text.

        Args:
            text (str): The help text to check
            cmd (BaseCommand): A command to check
        """
        for help_text in cmd.COMMAND_SPECIFICATION.command_help_text:
            self.assertIn(help_text, text,
                          f'has command help text {help_text}')

    def assertFlagHelpText(self, text: str, flag_spec: FlagSpecification):
        # This function name is kept this way to conform to assertEqual and
        # assertIn
        # pylint: disable=invalid-name
        """
        Asserts that the text contains the flag help text

        Args:
            text (str): The help text to check
            flag_spec (FlagSpecification): The flag spec to check against
        """
        name = flag_spec.name
        desc = flag_spec.help_text
        self.assertIn(name, text, f'has flag {name}')
        self.assertIn(desc, text, f'flag {name} also have help')

    def test_replace_help_flag(self):
        """
        Help flag should not be replaced.
        """
        with mock.patch.object(self.cmd.COMMAND_SPECIFICATION,
                               '_flag_specifications',
                               [FlagSpecification('h', int,
                                                  'A random flag')]):
            self.assertEqual(
                len(self.cmd.COMMAND_SPECIFICATION.flag_specifications), 2)
            generated_help = self.cmd.help()
            self.assertFlagHelpText(generated_help, HELP_FLAG)

    def test_help_generator_no_added_flags(self):
        """
        Commands should have themselves and all of their flags documented. This
        checks if the help flag is indeed documented.
        """
        generated_help = self.cmd.help()
        self.assertCommandHelpText(generated_help, self.cmd)
        self.assertFlagHelpText(generated_help, HELP_FLAG)

    def test_help_generator_with_added_flags(self):
        """
        Commands should have themselves and all of their flags documented. This
        checks if the help flag and all other flas are documented.
        """
        flag_spec = FlagSpecification('e', int, 'A random flag')
        with mock.patch.object(
                self.cmd.COMMAND_SPECIFICATION,
                '_flag_specifications',
                [flag_spec]):
            generated_help = self.cmd.help()
            self.assertCommandHelpText(generated_help, self.cmd)
            self.assertFlagHelpText(generated_help, HELP_FLAG)
            self.assertFlagHelpText(generated_help, flag_spec)

    def test_invalid_streams(self):
        """
        If, for any reason, someone passes in None for in_stream or out_stream,
        raise a skill issue error
        """
        with self.assertRaises(DeveloperSkillIssue):
            TestCommandFixture(None, StringIO(), [], [])

        with self.assertRaises(DeveloperSkillIssue):
            TestCommandFixture(StringIO(), None, [], [])

    def test_close(self):
        """
        Checks that if .close() is called, both input and output streams are
        closed.
        """
        self.cmd.close()
        self.assertTrue(self.cmd.input.closed)
        self.assertTrue(self.cmd.output.closed)


if __name__ == '__main__':
    unittest.main()
