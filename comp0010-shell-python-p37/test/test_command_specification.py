"""
This module tests the command specifications class
"""
import unittest
from unittest import mock

from commands.command_spec import CommandSpecification
from flag import FlagSpecification


class TestSpecifications(unittest.TestCase):
    """
    Tests command specifications
    """
    def setUp(self):
        self.spec = CommandSpecification(
            'unit_test_not_relevant', [], ('', ''))

    def test_with_no_added_flags(self):
        """
        When the implementing command does not have flags, there should only be
        one additional flag
        """
        self.assertEqual(
            len(self.spec.flag_specifications), 1)
        self.assertEqual(
            self.spec.flag_specifications[0].name, 'h')

    def test_with_one_added_flag(self):
        """
        When the implementing command has one flag, there should be two flags.
        """
        # decided to patch, since _acceptable_flags is protected
        with mock.patch.object(self.spec,
                               '_flag_specifications',
                               [FlagSpecification('e', int,
                                                  'A random flag')]):
            self.assertEqual(
                len(self.spec.flag_specifications), 2)
            only_flag_names = set(
                map(lambda x: x.name,
                    self.spec.flag_specifications))
            self.assertEqual({'h', 'e'}, only_flag_names)


if __name__ == '__main__':
    unittest.main()
