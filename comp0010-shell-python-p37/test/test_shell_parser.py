"""
Tests for the shell parser
"""
import unittest
from unittest.mock import MagicMock, patch

from commands.auto_import import AutoImport
from commands.echocommand import Echo
from errors.parse_errors import UserParseError
from parse.substitution_shell_parser import SubstitutionShellParser


class TestShellParser(unittest.TestCase):
    """
    Tests for the shell parser. The substitution shell parser encloses the raw
    shell parser, so testing the substitution shell parser will also test the
    raw shell parser. A little abstract, but this means we don't have to repeat
    tests
    """

    def setUp(self):
        self.mock_echo = MagicMock(spec=Echo)
        mock_auto_import = MagicMock(spec=AutoImport)
        mock_auto_import.get_command_objects.return_value = [self.mock_echo]
        with patch(
            "commands.auto_import.AutoImport", return_value=mock_auto_import
        ):
            self.parser = SubstitutionShellParser()

    def test_parse_single_command(self):
        """
        Tests that the parser can parse a command
        """
        cmdline = "echo Hello World"
        result = self.parser.parse(cmdline)
        self.assertEqual(
            result.command_type.COMMAND_SPECIFICATION.command_name, "echo"
        )
        self.assertEqual(result.options, ["Hello", "World"])

    def test_parse_error(self):
        """
        Tests that the parser can raise an error
        """
        cmdline = '"'
        with self.assertRaises(UserParseError):
            self.parser.parse(cmdline)


if __name__ == "__main__":
    unittest.main()
