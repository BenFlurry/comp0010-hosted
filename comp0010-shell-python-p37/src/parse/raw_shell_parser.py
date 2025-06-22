"""
This module contains the ShellParser class, which is used to parse command line
strings into a list of commands their arguments.

Classes:
    ShellParser: A class for parsing command line strings into a list of
    commands and their arguments.
"""
from typing import List, Optional

from commands.auto_import import AutoImport
from commands.builder import Builder
from parse.runner_visitor import RunnerVisitor

from .parse_tree_factory import create_parse_tree


class RawShellParser:
    # pylint: disable=too-few-public-methods
    """
    A class for parsing command line strings into a list of commands and their
    arguments.

    (Note: We don't use default arguments because pylint complains)
    """

    def __init__(self, commands: Optional[List[type]] = None):
        if commands is None:
            commands = AutoImport().get_command_objects()
        self.all_commands = commands

    def parse(self, cmdline: str) -> Builder:
        """
        Takes a Command Line string and returns a list of commands and their
        arguments

        Args:
            cmdline (str): The command line string to be parsed.

        Returns:
            Builder: List of tuples containing commands and their arguments
        """
        visitor = RunnerVisitor(self.all_commands)
        return visitor.visit(create_parse_tree(cmdline))
