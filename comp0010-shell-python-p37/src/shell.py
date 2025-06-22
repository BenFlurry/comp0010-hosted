"""
This module provides a command line interface to the PythonShell class through
direct inputs or command line arguments.
"""
import sys
import os
from io import StringIO
import readline

from python_shell import PythonShell
from errors.shell_errors import ShellExitError


if __name__ == "__main__":
    args_num = len(sys.argv) - 1
    if args_num > 0:
        if args_num != 2:
            raise ValueError("wrong number of command line arguments")
        if sys.argv[1] != "-c":
            raise ValueError(f"unexpected command line argument {sys.argv[1]}")
        with StringIO() as in_stream, StringIO() as out_stream:
            PythonShell(in_stream, out_stream).eval(sys.argv[2])
            out_stream.seek(0)
            print(out_stream.read(), end="")
    else:
        readline.parse_and_bind("tab: complete")
        while True:
            try:
                cmdline = input(os.getcwd() + "> ")
                with StringIO() as in_stream, StringIO() as out_stream:
                    PythonShell(in_stream, out_stream).eval(cmdline)
                    out_stream.seek(0)
                    print(out_stream.read(), end="")

            except KeyboardInterrupt:
                print("^C")
                continue
            except ShellExitError:
                sys.exit(0)
