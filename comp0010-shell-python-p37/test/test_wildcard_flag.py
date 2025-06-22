"""
Tests the WildcardFlagSpecification (ensures it throws all relevant errors)
"""

import unittest

from errors.error_dsi import DeveloperSkillIssue
from flag import WildcardFlagSpecification


class TestWildcardFlag(unittest.TestCase):
    """
     Wildcard flag specification is a special specification that will deny all
     attempts to get it's name, help text, and value. It is the parser's
     responsiblity to pass the flag as an option if it encounters a wildcard
     flag specification
    """

    def setUp(self):
        self.flag_spec = WildcardFlagSpecification()

    def test_getting_attributes(self):
        """
        Tries reading from the flag spec. A DeveloperSkillIssue should be
        thrown if any of the flag spec attributes are accessed.
        """
        # lambda is necessary, because name, value_type and help_text are
        # decorated as properties, so they evaluate immediately. This means you
        # get a DeveloperSkillIssue before the function can be passed to
        # assertRaises
        self.assertRaises(DeveloperSkillIssue, lambda: self.flag_spec.name)
        self.assertRaises(DeveloperSkillIssue,
                          lambda: self.flag_spec.value_type)
        self.assertRaises(DeveloperSkillIssue,
                          lambda: self.flag_spec.help_text)

    def test_writing_attributes(self):
        """
        Tries writing to the flag spec, it should basically do nothing and
        throw no throw an error. This is done this way because the base class'
        constructor writes to these variables; if these throw an error,
        everything breaks
        """
        self.flag_spec.name = ''
        self.flag_spec.flag_specifications = []
        self.flag_spec.help_text = ''

    def test_building_flag(self):
        """
        Tries to build a flag, but this should not work at all.
        """
        self.assertRaises(DeveloperSkillIssue,
                          self.flag_spec.build_flag_with_value, True)
