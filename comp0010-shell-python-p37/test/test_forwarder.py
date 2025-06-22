"""
This module tests the forwarder class
"""

import unittest
from io import StringIO

from commands.forwarder import Forwarder


class TestForwarder(unittest.TestCase):
    """
    Tests the forwarder class
    """
    def setUp(self):
        self.forwarder = Forwarder('stuff', StringIO(), 2)

    def test_run(self):
        """
        Tests that the forwarder, forwards the strings
        """
        self.assertEqual(self.forwarder.run(), 2)
        self.assertEqual(self.forwarder.out_stream.getvalue(), 'stuff\n')

    def test_close(self):
        """
        Tests that the stream is closed when the forwarder closes
        """
        self.forwarder.close()
        self.assertTrue(self.forwarder.out_stream.closed)


if __name__ == '__main__':
    unittest.main()
