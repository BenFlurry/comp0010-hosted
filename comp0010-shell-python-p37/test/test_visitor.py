"""
This module tests if the runner correctly interprets the command line.

It does so by ensuring the correct set of builders are returned; note that the
commands / pipes / sequences themselves will not run (these should be tested by
their respective unit tests).

This more or less uses a black-box testing approach; this class shouldn't call
the visit functions directly except for start()
"""


import unittest
from typing import List, Optional, Tuple, Type, Union, cast
from unittest.mock import patch

from parameterized import parameterized

from commands.base_command import BaseCommand
from commands.builder import Builder
from commands.catcommand import CAT
from commands.command_builder import CommandBuilder
from commands.command_spec import CommandSpecification
from commands.cutcommand import Cut
from commands.echocommand import Echo
from commands.redirect_builder import RedirectBuilder
from commands.unsafe_builder import UnsafeBuilder
from errors.error_dsi import DeveloperSkillIssue
from errors.parse_errors import (NoCommandError, UnknownCommandError,
                                 UnknownFlagError, UnknownFlagValueError)
from flag import FlagSpecification
from parse.substitution_shell_parser import SubstitutionShellParser
from parse.raw_shell_parser import RawShellParser


class MockCommand(BaseCommand):
    # pylint: disable=too-few-public-methods
    """
    A mock command, containing some flag specifications to test the parser
    """
    COMMAND_SPECIFICATION = CommandSpecification(
        "mock_command",
        [
            FlagSpecification("some_flag", bool, "testing flag"),
            FlagSpecification("other_flag", str, "other flag"),
            FlagSpecification("num_flag", int, "numerical flag"),
        ],
        ("", ""),
    )

    def run(self) -> int:
        """
        A fake run function for testing purposes
        """
        return 0


class TestRunnerVisitor(unittest.TestCase):
    """
    Tests the Runner visitor.
    """

    def create_mock_command_objects(self) -> List[Type[BaseCommand]]:
        """
        Creates a list of base commands available to the parser for this test
        """
        #  We're using echo here to help out with some flag-based testing,
        #  rather than reimplemnting echo.
        return [Echo, CAT, Cut, MockCommand]

    def perform_parsing_setup(self, cmdline: str) -> Builder:
        """
        Performs the lexer, token stream and parser setup required for parsing

        Arguments:
            cmdline (str): The command line to parse

        Returns:
            Builder: The builder returned by the visitor

        Raises:
            All exceptions throwablae by the runner visitor
        """
        return SubstitutionShellParser(
            self.create_mock_command_objects()).parse(cmdline)

    def assertMatchesCommandBuilder(
        self,
        builder: Builder,
        command_name: str,
        flags: List[Tuple[str, Union[str, bool, int]]],
        options: List[str],
    ):
        """
        Asserts that the builder matches a command builder with the right
        command names, flags and options.

        Arguments:
            builder (Builder): The builder to check against
            command_name (str): The expected command name
            flags (List[Tupe[str, Union[str, bool]]]):
                Flags expected. This is a list of tuples containing the flag
                name, and a value. In our context, this is either going ot be a
                string, boolean or int.
            options (List[str]): Options expected
        """
        # pylint: disable=invalid-name
        self.assertIsInstance(builder, CommandBuilder)
        # casting doesn't change builder. we're just making mypy happy
        builder = cast(CommandBuilder, builder)
        self.assertEqual(
            builder.command_type.COMMAND_SPECIFICATION.command_name,
            command_name,
        )
        flattened_flags = [(flag.name, flag.value) for flag in builder.flags]
        self.assertEqual(len(flags), len(flattened_flags))
        for flag in flags:
            self.assertIn(flag, flattened_flags, f"{flag} not present")

        self.assertEqual(len(options), len(builder.options))
        for option in options:
            self.assertIn(option, builder.options, f"{option} not present")

    @parameterized.expand([
        # Basic, straight-forward commands
        ('mock_command', 'mock_command', [], []),
        ('mock_command -some_flag', 'mock_command', [('some_flag', True)], []),
        ('mock_command -other_flag "hi"', 'mock_command',
         [('other_flag', 'hi')], []),
        ('mock_command -some_flag -other_flag "hi"',
         'mock_command', [('some_flag', True), ('other_flag', 'hi')], []),
        ('mock_command something',
         'mock_command', [], ['something']),
        ('mock_command -some_flag something -other_flag "hi"',
         'mock_command', [('some_flag', True), ('other_flag', "hi")],
         ['something']),
        ('echo hi', 'echo', [], ['hi']),
        ('echo "hello world"', 'echo', [], ["hello world"]),
        ('mock_command -other_flag 1-4', 'mock_command',
         [('other_flag', '1-4')], []),
        ('mock_command -other_flag "-4"', 'mock_command',
         [('other_flag', '-4')], []),
        ('mock_command -other_flag "1-"', 'mock_command',
         [('other_flag', '1-')], []),
        ('echo "\'\'\'"', 'echo', [], ["'''"]),
        ('echo "\'"Hello o/"\'"', 'echo', [], ["'Hello", "o/'"]),
        ("echo 'hello'", 'echo', [], ["hello"]),
        ("echo `echo hello ; echo world`", 'echo', [], ["hello", "world"]),

        # echo is slightly special; all unknown flags to it are also options.
        ('echo -flag', 'echo', [], ['-flag']),

        # cut is also special. all flags except -b and -h are options
        ('cut -b -4', 'cut', [('b', ['-4'])], []),
        ('cut -b -4 -h', 'cut', [('b', ['-4']), ('h', True)], []),

        # command substitution tests
        ('`echo mo`ck_command', 'mock_command', [], []),
        ('``mock_command', 'mock_command', [], []),
        ('` echo echo ` hello', 'echo', [], ['hello']),
        ('`echo mo`ck_comm`echo and`', 'mock_command', [], []),
        ('`echo mo``echo ck_comm``echo and`', 'mock_command', [], []),
        ('`echo mo`ck_command -`echo some`_flag "an"`echo _option`',
         'mock_command', [('some_flag', True)], ['an_option']),
        ('echo `echo "hello      world"`', 'echo', [], ['hello', 'world']),
        ('`echo echo hello wor`ld', 'echo', [], ['hello', 'world']),
        ('echo ``', 'echo', [], []),

        # partial escape tests
        (r'echo \'\'', 'echo', [], ['\'\'']),
        (r'echo \"', 'echo', [], ['"']),
        (r'echo \\', 'echo', [], ['\\']),
        (r'echo \\\\', 'echo', [], ['\\\\']),

        # quote combination test
        ('`"ec""ho" mo"ck"_command`', 'mock_command', [], []),

        # string literals test
        ('echo "-<>;|"', 'echo', [], ['-<>;|']),

        # Pipes
        ('echo `echo hello | cat`', 'echo', [], ['hello']),

        # Sequence
        ('echo `echo hi ; echo hello`', 'echo', [], ["hi", "hello"]),
    ])
    def test_commands(self,
                      cmdline: str,
                      command_name: str,
                      flags: List[Tuple[str, Union[str, bool, int]]],
                      options: List[str]):
        """
        Builds a command, expecting it to:
        1. Not throw an exception
        2. Parse flags and options correctly
        """
        self.assertMatchesCommandBuilder(
            self.perform_parsing_setup(cmdline), command_name, flags, options
        )

    @parameterized.expand(
        [
            ("", NoCommandError, "no command"),
            ("mock_command -f", UnknownFlagError, "Unknown flag f"),
            ("unknown_command", UnknownCommandError, "Unknown command"),
            (
                "mock_command -num_flag",
                UnknownFlagValueError,
                "requires a value",
            ),
            (
                "mock_command -num_flag -other_flag",
                UnknownFlagValueError,
                "requires a value",
            ),
            (
                "mock_command -num_flag bruh",
                UnknownFlagValueError,
                "Invalid value",
            ),
        ]
    )
    def test_commands_sad(
        self,
        cmdline: str,
        exception_cls: Type[BaseException],
        matching_regex: str,
    ):
        """
        Builds a command, expecting it to fail.
        """
        with self.assertRaisesRegex(exception_cls, matching_regex):
            self.perform_parsing_setup(cmdline)

    @parameterized.expand([
        ('echo hello', None, None),
        ('echo < hi.txt hello', 'hi.txt', None),
        ('echo > bye.txt hello', None, 'bye.txt'),
        ('echo < hi.txt hello > bye.txt', 'hi.txt', 'bye.txt'),
        ('< hi.txt echo', 'hi.txt', None),
        ('      < hi.txt echo', 'hi.txt', None),
        ('< hi.txt < bye.txt echo', 'bye.txt', None)
    ])
    def test_redirect(self,
                      cmdline: str,
                      expected_in_file: Optional[str],
                      expected_out_file: Optional[str]):
        """
        Tests redirects under above parameter circumstances
        """
        builder = self.perform_parsing_setup(cmdline)
        extracted_in, extracted_out = None, None
        while isinstance(builder, RedirectBuilder):
            if builder.in_file is not None and extracted_in is None:
                extracted_in = builder.in_file

            if builder.out_file is not None and extracted_out is None:
                extracted_out = builder.out_file
            builder = builder.child_buildable
        self.assertEqual(extracted_in, expected_in_file)
        self.assertEqual(extracted_out, expected_out_file)

    def test_unsafe(self):
        """
        Unsafe produces an unsafe builder that surrounds the underlying command
        """
        builder = self.perform_parsing_setup("_mock_command")
        self.assertIsInstance(builder, UnsafeBuilder)
        self.assertIsInstance(builder.wrapped_builder, CommandBuilder)
        self.assertEqual(
            builder.wrapped_builder.command_type.COMMAND_SPECIFICATION
            .command_name,
            "mock_command",
        )

    def test_do_not_allow_subcommands_in_raw(self):
        """
        RunnerVisitor should not allow subcommands.
        """
        with self.assertRaises(DeveloperSkillIssue):
            RawShellParser(self.create_mock_command_objects()).parse('`echo`')

    @parameterized.expand(
        [
            ("echo *", ["*"], []),
            ("echo *", ["hi.txt", "bye.txt"], ["hi.txt", "bye.txt"]),
        ]
    )
    def test_globbing_results_not_found(
        self, given_input: str, expected_output: List[str], matches: List[str]
    ):
        """
        Tests globbing where the globbing pattern matches no files
        """
        with patch("glob.glob", return_value=matches):
            builder = self.perform_parsing_setup(given_input)
            builder = cast(CommandBuilder, builder)
            self.assertIsInstance(builder, CommandBuilder)
            self.assertEqual(builder.options, expected_output)
