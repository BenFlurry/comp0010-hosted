"""
A visitor class for the command line parser grammar.
"""
import glob
from itertools import chain
from typing import Any, List, Optional, Tuple, Type

from antlr4 import TerminalNode  # type:ignore

from commands.base_command import BaseCommand
from commands.builder import Builder
from commands.command_builder import CommandBuilder
from commands.pipe_builder import PipeBuilder
from commands.redirect_builder import RedirectBuilder
from commands.runnable import Runnable
from commands.seq_builder import SeqBuilder
from commands.unsafe_builder import UnsafeBuilder
from errors.error_dsi import DeveloperSkillIssue
from errors.parse_errors import (NoCommandError, UnknownCommandError,
                                 UnknownFlagError, UnknownFlagValueError)
from flag import FlagSpecification, WildcardFlagSpecification
from parse.ParserGrammarParser import ParserGrammarParser
from parse.ParserGrammarVisitor import ParserGrammarVisitor

# We're conforming to ParserGrammerVisitor's naming convention
# pylint: disable=invalid-name


# Snake case violations are due to overriding methods from ANTLR4 generated
# classes
class RunnerVisitor(ParserGrammarVisitor):
    """
    A visitor class for the command line parser grammar. Callers must check if
    the 'eof_reached' attribute of the visitor has been returned; if it hasn't,
    the caller should call the parser again until all the commands have been
    evaluated.

    A reminder that subcommands work this way:
    - They are always executed first
    - Even if subcommands have a non-zero exit code, they will continue to
      execute.

    The following command: echo `invalid` world
        Will cause a normal Bash shell to first print that the command doesn't
        exist, then run echo on the output of the command substitution (empty
        string) and world, hence only printing world.

    This visitor should support arbitary placements of subcommands, including
    these monstrosities:

        - `echo ec`ho -spec`echo ial` he`echo llo` `echo wo`"r""ld"
        - `echo ex``echo claim``echo ation` > "some_"`cat testing1.txt`

    It was a design decision not to allow strings with \n, since the escape
    sequence is not implemented.
    """

    def __init__(self, command_list: List[Type[BaseCommand]]) -> None:
        self.flag_needs_value = False
        self.eof_reached = False
        self.builder_stack: List[CommandBuilder] = []
        self.command_list = command_list
        self.command_dict = {}
        for command in command_list:
            self.command_dict[
                command.COMMAND_SPECIFICATION.command_name
            ] = command

        super().__init__()

    def visitStart(self, ctx: ParserGrammarParser.StartContext) -> Runnable:
        # can't do visitChildren here, otherwise aggregateResult will be called
        child = ctx.getChild(0, ParserGrammarParser.CommandLineContext)
        if child is None:
            raise NoCommandError("there is no command to parse at start")
        return self.visit(
            ctx.getChild(0, ParserGrammarParser.CommandLineContext)
        )

    def visitCommandLine(
        self, ctx: ParserGrammarParser.CommandLineContext
    ) -> Builder:
        # Parser guarantees we'll get something visitable at this point
        return self.visit(ctx.getChild(0))

    @classmethod
    def handleWildcardFlagSpecification(
            cls,
            builder: CommandBuilder,
            text: str,
            backlog_flagspec: Optional[FlagSpecification]
    ) -> None:
        """
        Handles instances of WildcardFlagSpecification

        Args:
            builder (CommandBuilder): The command builder involved
            text (str): The flag name verbatim
            backlog_flagspec (Optional[FlagSpecification]): Any backlog flags
        """
        if backlog_flagspec is not None:
            flag = backlog_flagspec.build_flag_from_string(text)
            builder.add_flag(flag)
            return
        builder.add_option(text)

    @classmethod
    def handleFlagSpecification(
            cls,
            arg: FlagSpecification,
            builder: CommandBuilder,
            backlog_flagspec: Optional[FlagSpecification]
    ) -> Optional[FlagSpecification]:
        """
        Handles instances of FlagSpecification

        Args:
            arg (FlagSpecification): The Flag specification
            builder (CommandBuilder): The command builder involved
            backlog_flagspec (Optional[FlagSpecification]): Any backlog flag
        """
        if arg.value_type == bool:
            builder.add_flag(arg.build_flag_with_value(True))
            return backlog_flagspec
        # Encountering another flag while there is an unresolved
        # backlog flag means that the user has forgot to specify a
        # value. Stop parsing.
        if backlog_flagspec is not None:
            raise UnknownFlagValueError(
                f"Flag {backlog_flagspec.name} requires a value"
            )
        return arg

    @classmethod
    def handleFlagValue(cls, backlog_flagspec: FlagSpecification, arg: str,
                        builder: CommandBuilder) -> None:
        """
        Handles flag values based on the backlog flag specificaiton. This must
        exist.

        Args:
            builder (CommandBuilder): The command builder involved
            arg (str): The value verbatim
            backlog_flagspec (Optional[FlagSpecification]): Any backlog flag
        """
        flag = backlog_flagspec.build_flag_from_string(arg)
        builder.add_flag(flag)

    @classmethod
    def handleGlob(cls, arg: str, builder: CommandBuilder) -> None:
        """
        Handles Globs, like *.py.

        Args:
            builder (CommandBuilder): The command builder involved
            arg (str): The value verbatim
        """
        globs = glob.glob(arg)
        if len(globs) > 0:
            for globbed in globs:
                builder.add_option(globbed)
        else:
            builder.add_option(arg)

    def handleCommandArg(self, builder: CommandBuilder, arg: Any,
                         backlog_flagspec: Optional[FlagSpecification]
                         ) -> Tuple[CommandBuilder,
                                    Optional[FlagSpecification]]:
        """
        Handles arguments when visiting commands.

        Args:
            builder (CommandBuilder): The command builder involved
            arg (Any): Any object of any time. This function will filter and
                       redirect the call to the relevant handlers.
            backlog_flagspec (Optional[FlagSpecification]): Any backlog flag

        Returns:
            (Tuple[CommandBuilder, Optional[FlagSpecification]]):
                A tuple of the next command builder and new value of backlog
                flag
        """
        if isinstance(arg, tuple):
            if isinstance(arg[0], WildcardFlagSpecification):
                return (builder, self.handleWildcardFlagSpecification(
                    builder,
                    arg[1],
                    backlog_flagspec))

            # arg[0] must be a FlagSpecification
            return (builder, self.handleFlagSpecification(
                arg[0], builder, backlog_flagspec))

        if isinstance(arg, RedirectBuilder):
            # Update the builder to use the current builder
            builder = arg
            self.builder_stack[-1] = builder

        if isinstance(arg, str):
            if backlog_flagspec is not None:
                return (builder, self.handleFlagValue(
                    backlog_flagspec, arg, builder))

            self.handleGlob(arg, builder)

        return (builder, None)

    def visitCommand(self, ctx: ParserGrammarParser.CommandContext) -> Builder:
        # Create a command builder for the command
        literal_app_name = self.visit(ctx.name())
        is_unsafe = literal_app_name[0] == "_"
        app_name = literal_app_name[int(is_unsafe):]
        if app_name not in self.command_dict:
            raise UnknownCommandError(f"Unknown command {app_name}")
        app = self.command_dict[app_name]
        builder = CommandBuilder(app)

        self.builder_stack.append(builder)
        backlog_flagspec: Optional[FlagSpecification] = None
        # we need the laziness of map rather than list comprehension to
        # properly utilize the builder_stack; if we use list comprehension,
        # `builder`'s 2 RedirectBuilders will not affect each other, which is
        # intended behaviour.
        for arg in map(self.visit, chain(ctx.redirect(), ctx.modifier())):
            builder, backlog_flagspec = self.handleCommandArg(
                builder, arg, backlog_flagspec)

        if backlog_flagspec is not None:
            raise UnknownFlagValueError(
                f"Flag {backlog_flagspec.name} requires a value"
            )
        self.builder_stack.pop()
        return builder if not is_unsafe else UnsafeBuilder(builder)

    def visitPipe(self, ctx: ParserGrammarParser.PipeContext) -> Builder:
        builders = list(
            filter(
                lambda x: issubclass(type(x), Builder),
                (self.visit(child) for child in ctx.getChildren()),
            )
        )

        return PipeBuilder(builders[0], builders[1])

    def visitSequence(
        self, ctx: ParserGrammarParser.SequenceContext
    ) -> Builder:
        b = [self.visit(builder) for builder in ctx.getChildren()]
        left, right = [x for x in b if not isinstance(x, str)]
        # Sequences have a pair of builders of any type
        return SeqBuilder(left, right)

    def visitModifier(
        self, ctx: ParserGrammarParser.ModifierContext
    ) -> FlagSpecification:
        # can't do visitChildren here, otherwise aggregateResult will be called
        return self.visit(ctx.getChild(0))

    def visitFlag(
        self, ctx: ParserGrammarParser.FlagContext
    ) -> Tuple[FlagSpecification, str]:
        # Get just the WORD representing the flag
        # Associating the flag with its value is done in visitCommand
        flag = self.visit(ctx.getChild(1))
        flag_specifications = self.builder_stack[
            -1
        ].command_type.COMMAND_SPECIFICATION.flag_specifications
        for flag_spec in flag_specifications:
            if (
                isinstance(flag_spec, WildcardFlagSpecification)
                or flag_spec.name == flag
            ):
                return (flag_spec, '-' + flag)
        raise UnknownFlagError(f"Unknown flag {flag}")

    def visitRedirect(
        self, ctx: ParserGrammarParser.RedirectContext
    ) -> RedirectBuilder:
        direction = ctx.getChild(0).getText()
        file = ctx.phrase().getText()
        builder = RedirectBuilder(self.builder_stack[-1])
        if direction == "<":
            builder.set_in_file(file)
        else:
            builder.set_out_file(file)
        return builder

    def visitSubcommand(
        self, ctx: ParserGrammarParser.SubcommandContext
    ) -> str:
        raise DeveloperSkillIssue(
            "The command line must first go through the substitution visitor")

    def visitLiteral(self, ctx: ParserGrammarParser.LiteralContext) -> str:
        # every literal is either a CHAR or one of "|;<>. Hence, we simply get
        # the concatenated text.
        return ("".join([child.getText() for child in ctx.children]))

    def visitDq_string(self, ctx: ParserGrammarParser.Dq_stringContext) -> str:
        # first and last child are guaranteed to be the quotes (otherwise the
        # parser should have failed). Everything else needs to become a string.
        return "".join([self.visit(child) for child in ctx.children[1:-1]])

    def visitSq_string(self, ctx: ParserGrammarParser.Sq_stringContext) -> str:
        return "".join([self.visit(child) for child in ctx.children[1:-1]])

    def aggregateResult(self, aggregate: str, nextResult: str) -> str:
        """
        aggregateResult is an ANTLR-provided function that combines the results
        of the ANTLR parser into one.

        In the case of our visitor, it is used more or less solely for
        visitPhrase.
        """
        return aggregate + nextResult

    def visitTerminal(self, node: TerminalNode) -> str:
        """
        visitTerminal is an ANTLR-provided function that runs whenever a
        terminal is visited. In our visitor and parser combo, the only
        terminals we'll reach are SPACE, CHARS and the other separators
        such as ', ", |, ;, <, `, etc.

        ` should return empty because that is the empty command substitution
        which is a special case

        Returns:
            str: The terminal node interpreted as a reasonable string
        """
        text = (node.getText()
                .replace('\\\'', '\'')
                .replace('\\"', '"')
                .replace('\\\\', '\\'))
        return text if text != '`' else ''

    def defaultResult(self) -> str:
        """
        defaultResult is an ANTLR-provided function that runs whenever there is
        an unresolved terminal. In our visitor and parser combo, the only
        temrinals we'll reach are SPACE, WORD and STRING.

        Returns: str: The empty string
        """
        return ""
