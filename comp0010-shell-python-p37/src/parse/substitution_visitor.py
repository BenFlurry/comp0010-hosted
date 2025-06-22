"""
A visitor class to do command substitution.

Originally, runner_visitor.py was designed to perform substitution.  However,
to support `echo echo hello wor`ld, which results in "hello world", a separate
visitor is necessary.

Also, only Level 1 substitution is supported (i.e. backslash` will not be
interpreted again). In other words, nested substitution is not supported.

The caller must call SubstitutionVisitor before calling RunnerVisitor
"""
from io import StringIO

from antlr4 import TerminalNode  # type:ignore
from antlr4 import Token  # type: ignore

from parse.ParserGrammarParser import ParserGrammarParser
from parse.ParserGrammarVisitor import ParserGrammarVisitor

from .raw_shell_parser import RawShellParser


class SubstitutionVisitor(ParserGrammarVisitor):
    """
    A visitor class that performs command substitution.

    Internally, this class uses the RunnerVisitor to run the command
    substitution
    """
    def visitSubcommand(
        self, ctx: ParserGrammarParser.SubcommandContext
    ) -> str:
        cmd_line = ctx.commandLine()
        if not cmd_line:
            # this case occurs if we receive an empty ``
            return ""

        out_stream = StringIO()
        runnable = (RawShellParser().parse(cmd_line.getText())
                    .set_out_stream(out_stream).build())
        with runnable:
            # in bash, all leading and trailing newlines are stripped in
            # subcommands
            runnable.run()
            return ' '.join(d for d in out_stream
                            .getvalue()
                            .replace("\n", " ")
                            .replace('"', '\\"')
                            .replace("'", "\\'")
                            .strip()
                            .split(' ') if d != '')

    def aggregateResult(self, aggregate: str, nextResult: str) -> str:
        return aggregate + nextResult

    def visitTerminal(self, node: TerminalNode) -> str:
        if node.getSymbol().type == Token.EOF:
            return ''
        return node.getText()

    def defaultResult(self) -> str:
        return ""
