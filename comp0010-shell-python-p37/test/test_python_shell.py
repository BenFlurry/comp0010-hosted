"""
This is a test for the PythonShell class
"""
import unittest
from io import StringIO, TextIOBase
from types import TracebackType
from typing import ContextManager, Optional, Type
from unittest.mock import MagicMock, patch, create_autospec

from typing_extensions import Literal, Self

from commands.builder import Builder
from commands.runnable import Runnable
from errors.command_errors import CommandError
from errors.shell_errors import ShellExitError
from python_shell import PythonShell


class MockBuilder(ContextManager, Builder):
    """
    A mock builder for testing. Needs to write to the given stream for testing
    so a magic mock was not appropriate
    """

    def __init__(self, output) -> None:
        self.in_stream: TextIOBase = StringIO()
        self.out_stream: TextIOBase = StringIO()
        self.output = output

    def set_in_stream(self, in_stream: TextIOBase) -> Self:
        self.in_stream = in_stream
        return self

    def set_out_stream(self, out_stream: TextIOBase) -> Self:
        self.out_stream = out_stream
        return self

    def build(self) -> Runnable:
        mock = create_autospec(Runnable)
        mock.__enter__.side_effect = self.__enter__
        mock.run.side_effect = self.run
        mock.__exit__.side_effect = self.__exit__
        return mock

    def run(self) -> int:
        """
        Stubbed run function that just writes output. This is passed as a mock
        """
        self.out_stream.write(self.output)
        self.out_stream.seek(0)
        return 0

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exception_type: Optional[Type[BaseException]],
        exception_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> Literal[False]:
        self.out_stream.close()
        self.in_stream.close()
        return False  # propagate errors


class TestPythonShell(unittest.TestCase):
    """
    A class for testing the PythonShell class
    """

    def setUp(self) -> None:
        self.out: StringIO = StringIO()

    def tearDown(self):
        self.out.close()

    def test_normal(self):
        """
        Tests a normal command line
        """
        mock_builder = MockBuilder("test ouput")
        with patch(
            "parse.substitution_shell_parser.SubstitutionShellParser.parse",
                return_value=mock_builder
        ):
            PythonShell(StringIO(), self.out).eval("test")
            self.assertEqual(self.out.read(), "test ouput")

    def test_base_shell_error(self):
        """
        Tests command line error catching
        """
        with patch(
            "parse.substitution_shell_parser.SubstitutionShellParser.parse",
            side_effect=CommandError("Test Error"),
        ), patch("sys.stderr", object=MagicMock()) as mock_errorout:
            PythonShell(StringIO(), self.out).eval("test")
            mock_errorout.write.assert_called_once_with(
                "Command, CommandError: Test Error\n"
            )

    def test_other_error(self):
        """
        Tests other errors
        """
        with patch(
            "parse.substitution_shell_parser.SubstitutionShellParser.parse",
                side_effect=Exception
        ):
            with self.assertRaises(Exception):
                PythonShell(StringIO(), self.out).eval("test")

    def test_exit(self):
        """
        Tests exit
        """
        with self.assertRaises(ShellExitError):
            PythonShell(StringIO(), self.out).eval("exit")


if __name__ == "__main__":
    unittest.main()
