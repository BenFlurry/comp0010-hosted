"""
A module that contains unit tests for the echo command.
"""
import unittest
from io import StringIO

from commands.echocommand import Echo


class TestEcho(unittest.TestCase):
    """
    A test class for the Echo class.
    """

    def setUp(self) -> None:
        self.in_stream = StringIO()
        self.out_stream = StringIO()

    def test_echo_normal(self):
        """
        Test the Echo class with a single option.
        """
        flags = []
        options = ["hello world"]
        echo = Echo(self.in_stream, self.out_stream, flags, options)
        echo.run()
        self.assertEqual(echo.output.getvalue(), "hello world\n")

    def test_echo_multiple_options(self):
        """
        Test the Echo class with multiple options.
        """
        flags = []
        options = ["hello", "world", 'this', 'is', 'a', 'test']
        echo = Echo(self.in_stream, self.out_stream, flags, options)
        echo.run()
        self.assertEqual(echo.output.getvalue(),
                         "hello world this is a test\n")

    def test_echo_no_options(self):
        """
        Test the Echo class with no options.
        """
        flags = []
        options = []
        echo = Echo(self.in_stream, self.out_stream, flags, options)
        echo.run()
        self.assertEqual(echo.output.getvalue(), "\n")


if __name__ == "__main__":
    unittest.main()
