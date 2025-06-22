"""
Module to test the unsafe decorator
"""

import unittest
from io import StringIO
from unittest.mock import MagicMock

from commands.unsafe_decorator import UnsafeDecorator
from errors.command_errors import BaseShellError


class TestUnsafeDecorator(unittest.TestCase):
    """
    All (known) errors that occur should be caught by the unsafe decorator.
    This class tests that assumption.
    """
    def setUp(self):
        self.runnable = MagicMock()
        self.out_stream = StringIO()
        self.unsafe = UnsafeDecorator(self.runnable, self.out_stream)

    def test_run_happy(self):
        """
        When the wrapped command runs perfectly fine, the decorator should
        just return the return code directly
        """
        def side_effect() -> int:
            self.out_stream.write('hi')
            return 42069
        self.runnable.run.side_effect = side_effect
        self.assertEqual(self.unsafe.run(), 42069)
        self.assertEqual(self.out_stream.getvalue(), 'hi')
        self.runnable.run.assert_called_once()

    def test_run_sad(self):
        """
        When the wrapped command throws an exception, the decorator should
        catch it and redirect error messages to the output
        """
        self.runnable.run.side_effect = BaseShellError('some error')
        self.assertEqual(self.unsafe.run(), 1)
        self.assertEqual(self.out_stream.getvalue(), 'some error\n')
        self.runnable.run.assert_called_once()

    def test_close(self):
        """
        Close should call the child's close
        """
        self.unsafe.close()
        self.runnable.close.assert_called_once()
        self.assertTrue(self.out_stream.closed)


if __name__ == '__main__':
    unittest.main()
