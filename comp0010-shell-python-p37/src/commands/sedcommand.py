"""
Sed command, implemented only exactly to spec.
"""
import re
from io import StringIO, TextIOWrapper
from re import Pattern
from typing import List

from commands.base_command import BaseCommand
from commands.command_helpers import exception_handled_open, is_stream_empty
from commands.command_spec import CommandSpecification
from errors.command_errors import CommandError
from flag import FlagValue


class Sed(BaseCommand):
    """
    Only supports the s/ prefix and /g suffix. With the s/ prefix, Sed performs
    regex substitution, although only a limited set will be implemented here
    (e.g. no fancy grouping substitution). With the /g suffix, replaces ALL
    instances. Without the /g suffix, replaces the FIRST instance.

    All substitution is performed on a per-newline basis.
    """
    COMMAND_SPECIFICATION = \
        CommandSpecification("sed", [],
                             ("Expression [FILE]",
                              "A limited sed that performs only s/ prefix and"
                              " supports only the /g suffix. If no file is "
                              " specified, will use STDIN."))

    def __init__(self,
                 in_stream: StringIO,
                 out_stream: StringIO,
                 flags: List[FlagValue],
                 options: List[str]) -> None:
        super().__init__(in_stream, out_stream, flags, options)
        self.replace_from: Pattern[str] = re.compile('')
        self.replace_to: str = r''
        self.replace_global = False
        self.__options_guard()

    def __expression_guard(self, expression: str):
        """
        Throws an exception if the expression is not supported by this
        function.

        Requires 4 segments, with one of the two delimiters (either / or |).
        Requires the s/ or s| prefix, and either the existence (or lack
        thereof) of 'g'
        """
        if expression[:2] != 's/' and expression[:2] != 's|':
            raise CommandError("Unsupported sed prefix")

        if expression[-2:] == '/g' or expression[-2:] == '|g':
            self.replace_global = True

        sep = expression[1]  # s/ or s| from above, so [1] is either / or |
        # it is not possible to get anything other than / or | due to above
        # check

        splitted = expression.split(sep)
        # there must be 4 splits for the expr to be valid
        # s/hi/bye/g (s,hi,bye,g)
        # s/hi/bye/ (s,hi,bye,)
        if len(splitted) != 4:
            raise CommandError("Invalid expression")

        (_, replace_from_str, replace_to_str, _) = splitted
        try:
            self.replace_from = re.compile(replace_from_str)
            self.replace_to = replace_to_str
        except re.error as e:
            raise CommandError("Invalid pattern") from e

    def __options_guard(self):
        if len(self.options) < 1:
            raise CommandError("Not enough arguments to command")
        self.__expression_guard(self.options[0])

    def _sed(self, in_stream: TextIOWrapper, out_stream: TextIOWrapper) \
            -> None:
        """
        Processes the sed command, replacing arbitrary strings from the
        in_stream to the out_stream (these are parameters).

        This function assumes that self has been correctly configured.

        Args:
            in_stream (TextIOWrapper): The input stream to run sed on
            out_stream (TextIOWrapper): The output stream to dump sed output
        """
        for line in in_stream:
            out_stream.write(
                self.replace_from.sub(
                    self.replace_to, line,
                    count=int(not self.replace_global)))

    def run(self) -> int:
        """
        see BaseCommand.run()
        """
        if len(self.options) < 2:
            if is_stream_empty(self.input):
                raise CommandError("No input provided")
            self._sed(self.input, self.output)
            return 0

        file = self.options[1]
        with exception_handled_open(file, 'r') as f:
            self._sed(f, self.output)
        return 0
