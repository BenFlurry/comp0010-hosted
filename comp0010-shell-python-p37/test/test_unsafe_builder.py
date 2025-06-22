"""
A module to test the unsafe builder.
"""
import unittest
from io import StringIO
from unittest.mock import MagicMock

from commands.builder import Builder
from commands.forwarder import Forwarder
from commands.runnable import Runnable
from commands.unsafe_builder import UnsafeBuilder
from commands.unsafe_decorator import UnsafeDecorator
from errors.command_errors import BaseShellError


class TestUnsafeBuilder(unittest.TestCase):
    """
    Tests the unsafe builder
    """
    def setUp(self):
        self.builder = MagicMock(spec=Builder)
        self.result_runnable = MagicMock()
        self.in_stream, self.out_stream = StringIO(), StringIO()
        self.unsafe_builder = UnsafeBuilder(self.builder)
        self.unsafe_builder.set_in_stream(self.in_stream)
        self.unsafe_builder.set_out_stream(self.out_stream)

        self.builder.build.return_value = self.result_runnable

    def base_build_and_asserts(self) -> Runnable:
        """
        When building any unsafe builder, ensures the builder sets the child's
        in and out streams
        """
        runnable = self.unsafe_builder.build()
        self.builder.set_in_stream.assert_called_once_with(self.in_stream)
        self.builder.set_out_stream.assert_called_once_with(self.out_stream)
        self.builder.build.assert_called_once()
        return runnable

    def test_build(self):
        """
        If the underlying builder does not throw an exception during a build,
        we wrap the result Runnable into an unsafe decorator
        """
        decorator = self.base_build_and_asserts()
        self.assertIsInstance(decorator, UnsafeDecorator)
        self.assertEqual(decorator.wrapped_runnable, self.result_runnable)

    def test_build_with_exception(self):
        """
        If the underlying builder throws an exception during a build, the
        exception should be wrapped in a Forwarder runnable.
        """
        self.builder.build.side_effect = BaseShellError(
            'one of the errors of all time')
        forwarder = self.base_build_and_asserts()
        self.assertIsInstance(forwarder, Forwarder)
        self.assertEqual(forwarder.forwarded_string,
                         'one of the errors of all time')


if __name__ == '__main__':
    unittest.main()
