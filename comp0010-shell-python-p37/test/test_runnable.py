"""
Tests the runnable module. Makes sure that the context manager has some
coverage.
"""

import unittest
from unittest import mock

from commands.runnable import Runnable


class TestRunnable(unittest.TestCase):
    """
    Tests the runnable with the mock runnable fixture
    """
    def setUp(self):
        self.runnable = mock.create_autospec(Runnable)
        self.runnable.run.return_value = 0
        self.runnable.run_and_close = Runnable.run_and_close
        self.runnable.__enter__ = Runnable.__enter__
        self.runnable.__exit__ = Runnable.__exit__

    def test_run_and_exit(self):
        """
        Checks that with the run_and_close function, the close() function is
        called
        """
        # For some reason, I can't get self.runnable.run_and_close() to work,
        # so instead I'll do something equivalent
        self.assertEqual(Runnable.run_and_close(self.runnable), 0)
        self.runnable.close.assert_called_once_with()


if __name__ == '__main__':
    unittest.main()
