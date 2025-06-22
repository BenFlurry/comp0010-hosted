"""
Package contains flags used throughout the program
"""

# Unused imports disabled because the lines below re-exports
# pylint: disable=unused-import
# flake8: noqa=F401

from .flag import Flag, FlagSpecification, FlagValue
from .wildcard_flag import WildcardFlagSpecification
