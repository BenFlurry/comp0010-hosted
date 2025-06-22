"""
A module implementing a bash style shell in python
"""

import sys
from io import StringIO

from errors.errors import BaseShellError
from errors.shell_errors import ShellExitError
from parse.substitution_shell_parser import SubstitutionShellParser

# pylint: disable=too-few-public-methods
# Python shell only needs an eval method


class PythonShell:
    """
    A class representing a python shell
    """

    def __init__(self, in_stream: StringIO, out_stream: StringIO):
        self.in_stream: StringIO = in_stream
        self.out_stream: StringIO = out_stream

    def eval(self, cmdline: str):
        """
        Evaluates a command line.
        Args:
            cmdline: The command line to evaluate
            out: The output deque

        Returns:
            None
        """

        parser = SubstitutionShellParser()
        try:
            builder = parser.parse(cmdline)
            out = StringIO()
            runnable = (
                builder.set_in_stream(self.in_stream)
                .set_out_stream(out)
                .build()
            )
            # The following ensures that the runnable streams are closed after
            # it is run, so the contents of out need to be copied into the
            # out_stream before it is closed.
            with runnable as r:
                r.run()
                out.seek(0)
                self.out_stream.write(out.read())
        except ShellExitError as e:
            raise e
        except BaseShellError as e:
            sys.stderr.write(f"{e}\n")
        self.out_stream.seek(0)
