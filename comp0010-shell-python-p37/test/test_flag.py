"""
Tests the FlagSpecification building
"""

import unittest
from typing import List

from errors.error_dsi import DeveloperSkillIssue
from flag import FlagSpecification


class TestFlag(unittest.TestCase):
    """
    Tests building flags with flag specifications
    """
    def setUp(self):
        self.flag_spec = FlagSpecification[str]('e', str, 'testing flag')

    def test_building_valid_flag(self):
        """
        Can builds a valid flag (i.e. types match)
        """
        flag_value = 'A value'
        flag = self.flag_spec.build_flag_with_value(flag_value)
        self.assertEqual(flag.name, self.flag_spec.name)
        self.assertEqual(flag.value, flag_value)
        self.assertEqual(flag.help_text, self.flag_spec.help_text)

    def test_building_valid_flag_from_string(self):
        """
        Can build valid flag (trivial)
        """
        value = 123
        flag_spec = FlagSpecification[int]('e', int, 'testing')
        flag = flag_spec.build_flag_from_string(str(value))
        self.assertEqual(flag.value, value)

    def test_building_valid_flag_array_from_string(self):
        """
        Can build a flag array
        """
        flag_spec = FlagSpecification[List[int]]('e', List[int], 'testing')
        flag = flag_spec.build_flag_from_string('1,2,3')
        self.assertEqual(flag.value, [1, 2, 3])

    def test_building_invalid_flag(self):
        """
        Cannot build an invalid flag (i.e. types do not match)
        """
        flag_value = 10
        with self.assertRaises(DeveloperSkillIssue):
            self.flag_spec.build_flag_with_value(flag_value)

    def test_building_invalid_flag_none(self):
        """
        Cannot build an invalid flag (i.e. types do not match)
        """
        flag_value = None
        with self.assertRaises(DeveloperSkillIssue):
            self.flag_spec.build_flag_with_value(flag_value)
