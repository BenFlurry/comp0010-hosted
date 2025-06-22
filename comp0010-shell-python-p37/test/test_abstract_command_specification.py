"""
Ensures that the abstract command specification throws an error if it's not
implemented
"""

import unittest
from typing import Callable

from parameterized import parameterized

from commands.command_spec import AbstractCommandSpecification
from errors.error_dsi import DeveloperSkillIssue


class TestAbstractCommandSpecification(unittest.TestCase):
    """
    AbstractCommandSpecification is special, because it is not meant to be
    instantiated. If it is instantiated and any of the properties are called,
    then it was not overriden and should throw errors.
    """

    def setUp(self):
        self.cmd_spec = AbstractCommandSpecification()

    @parameterized.expand({
        (lambda x: x.command_name,),
        (lambda x: x.flag_specifications,),
        (lambda x: x.command_help_text,)
    })
    def test_throws_dsi(self, fn: Callable[[AbstractCommandSpecification],
                                           None]):
        """
        All command specification properties should raise an error when invoked
        """
        with self.assertRaises(DeveloperSkillIssue):
            fn(self.cmd_spec)
