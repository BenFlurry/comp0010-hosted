"""
This module contains the substitution parser, which parses all command
substitution strings.

Classes:
    SubstitutionParser: A parser for parsing substitutions within command line
    strings.
"""
from commands.builder import Builder
from parse.substitution_visitor import SubstitutionVisitor

from .parse_tree_factory import create_parse_tree
from .raw_shell_parser import RawShellParser


class SubstitutionShellParser(RawShellParser):
    # pylint: disable=too-few-public-methods
    """
    A class for parsing command line strings into a list of commands and their
    arguments.
    """
    def parse(self, cmdline: str) -> Builder:
        """
        Takes a Command Line string and returns a fully substituted string

        Args:
            cmdline (str): The command line string to be parsed.

        Returns:
            str: The substitution that is fully substituted
        """
        visitor = SubstitutionVisitor()
        return RawShellParser(self.all_commands).parse(
            visitor.visit(create_parse_tree(cmdline)))
