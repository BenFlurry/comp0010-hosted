"""
Tests Redirect Builder
"""

import unittest
from io import StringIO
from typing import List, Optional, Tuple, Type
from unittest.mock import MagicMock, mock_open, patch

from parameterized import parameterized

from commands.base_command import BaseCommand
from commands.command_builder import CommandBuilder
from commands.redirect import Redirect
from commands.redirect_builder import RedirectBuilder
from errors.command_errors import ShellFileNotFoundError
from errors.redirect_errors import RedirectError
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


class TestRedirectBuilder(unittest.TestCase):
    """
    Tests that the redirect builder passes the right stuff to the command when
    it is being built
    """
    def make_redirect_builder_with(self,
                                   in_stream: Optional[StringIO],
                                   out_stream: Optional[StringIO]
                                   ) -> Tuple[RedirectBuilder, MagicMock]:
        """
        Creates a redirect builder with the given input and output streams.

        Args:
            in_stream (Optional[StringIO]): The input stream to build with
            out_stream (Optional[StringIO]): The output stream to build with

        Returns:
            (Tuple[RedirectBuilder, MockedCommandBuilder])
        """
        mock_command_builder = MagicMock()
        mock_command_builder.set_in_stream = MagicMock(
            wraps=lambda x: CommandBuilder.set_in_stream(mock_command_builder,
                                                         x))
        mock_command_builder.set_out_stream = MagicMock(
            wraps=lambda x: CommandBuilder.set_out_stream(mock_command_builder,
                                                          x))
        redirect_builder = RedirectBuilder(mock_command_builder)
        if in_stream is not None:
            redirect_builder.set_in_stream(in_stream)

        if out_stream is not None:
            redirect_builder.set_out_stream(out_stream)

        return redirect_builder, mock_command_builder

    def test_happy_redirect_builder(self):
        """
        In the base case, the redirect builder should build a runnable that
        """
        in_stream, out_stream = StringIO(), StringIO()
        redirect_builder, cmd_builder_mock = self.make_redirect_builder_with(
            in_stream,
            out_stream
        )
        redirect = redirect_builder.build()
        self.assertIsInstance(redirect, Redirect)
        self.assertEqual(redirect.in_stream, in_stream)
        self.assertEqual(redirect.out_stream, out_stream)
        cmd_builder_mock.set_in_stream.assert_called_once()
        cmd_builder_mock.set_out_stream.assert_called_once()

    def test_happy_redirect_builder_from_in_file(self):
        """
        In the case where there is an in_file, building the redirect should
        open the file.
        """
        in_stream, out_stream = StringIO(), StringIO()
        redirect_builder, _ = self.make_redirect_builder_with(
            in_stream,
            out_stream
        )
        redirect_builder.set_in_file("test_file")
        open_fn = mock_open()

        with patch('builtins.open', open_fn):
            redirect = redirect_builder.build()
            self.assertIsInstance(redirect, Redirect)
            open_fn.assert_called_once_with('test_file')
            self.assertNotEqual(redirect.in_stream, in_stream)
            self.assertEqual(redirect.out_stream, out_stream)

    def test_happy_redirect_builder_to_out_file(self):
        """
        In the case where there is an out_file, building the redirect should
        open the file.
        """
        in_stream, out_stream = StringIO(), StringIO()
        redirect_builder, _ = self.make_redirect_builder_with(
            in_stream,
            out_stream
        )
        redirect_builder.set_out_file("test_file")
        open_fn = mock_open()

        with patch('builtins.open', open_fn):
            redirect = redirect_builder.build()
            self.assertIsInstance(redirect, Redirect)
            open_fn.assert_called_once_with('test_file', 'w')
            self.assertEqual(redirect.in_stream, in_stream)
            self.assertNotEqual(redirect.out_stream, out_stream)

    def test_happy_redirect_builder_to_in_and_out_file(self):
        """
        In the case where there is an out_file, building the redirect should
        open the file.
        """
        in_stream, out_stream = StringIO(), StringIO()
        redirect_builder, _ = self.make_redirect_builder_with(
            in_stream,
            out_stream
        )
        redirect_builder.set_in_file("in_file").set_out_file("out_file")
        open_fn = mock_open()

        with patch('builtins.open', open_fn):
            redirect = redirect_builder.build()
            self.assertIsInstance(redirect, Redirect)
            open_fn.assert_any_call('in_file')
            open_fn.assert_any_call('out_file', 'w')
            self.assertNotEqual(redirect.in_stream, in_stream)
            self.assertNotEqual(redirect.out_stream, out_stream)

    def test_happy_redirect_builder_propagates_setters_downards(self):
        """
        The other functions of RedirectBuilder, such as add_flag and add_option
        should propagate downwards to the CommandBuilder
        """
        in_stream, out_stream = StringIO(), StringIO()
        redirect_builder, cmd_builder = self.make_redirect_builder_with(
            in_stream,
            out_stream
        )
        flag = Flag[int]('r', 100, 'a flag')
        redirect_builder.add_flag(flag)
        redirect_builder.add_option('test')
        cmd_builder.add_flag.assert_called_with(flag)
        cmd_builder.add_option.assert_called_with('test')

    @parameterized.expand({
        (FileNotFoundError, ShellFileNotFoundError, ''),
        (PermissionError, RedirectError, 'unable.*one'),
        (IsADirectoryError, RedirectError, 'unexpected'),
        (OSError, RedirectError, 'unknown')
    })
    def test_exceptions(self,
                        open_raises_cls: Type[BaseException],
                        target_exception_cls: Type[BaseException],
                        target_regex_str: str):
        """
        Checks if the builder raises the right exceptions under certain
        circumstances
        """
        in_stream, out_stream = StringIO(), StringIO()
        redirect_builder, _ = self.make_redirect_builder_with(
            in_stream,
            out_stream
        )
        redirect_builder.set_in_file('does not matter')
        with patch('builtins.open', side_effect=open_raises_cls()):
            with self.assertRaisesRegex(
                    target_exception_cls, target_regex_str):
                redirect_builder.build()


if __name__ == '__main__':
    unittest.main()
