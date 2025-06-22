# Generated from ParserGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ParserGrammarParser import ParserGrammarParser
else:
    from ParserGrammarParser import ParserGrammarParser

# This class defines a complete listener for a parse tree produced by ParserGrammarParser.
class ParserGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by ParserGrammarParser#start.
    def enterStart(self, ctx:ParserGrammarParser.StartContext):
        pass

    # Exit a parse tree produced by ParserGrammarParser#start.
    def exitStart(self, ctx:ParserGrammarParser.StartContext):
        pass


    # Enter a parse tree produced by ParserGrammarParser#commandLine.
    def enterCommandLine(self, ctx:ParserGrammarParser.CommandLineContext):
        pass

    # Exit a parse tree produced by ParserGrammarParser#commandLine.
    def exitCommandLine(self, ctx:ParserGrammarParser.CommandLineContext):
        pass


    # Enter a parse tree produced by ParserGrammarParser#command.
    def enterCommand(self, ctx:ParserGrammarParser.CommandContext):
        pass

    # Exit a parse tree produced by ParserGrammarParser#command.
    def exitCommand(self, ctx:ParserGrammarParser.CommandContext):
        pass


    # Enter a parse tree produced by ParserGrammarParser#pipe.
    def enterPipe(self, ctx:ParserGrammarParser.PipeContext):
        pass

    # Exit a parse tree produced by ParserGrammarParser#pipe.
    def exitPipe(self, ctx:ParserGrammarParser.PipeContext):
        pass


    # Enter a parse tree produced by ParserGrammarParser#sequence.
    def enterSequence(self, ctx:ParserGrammarParser.SequenceContext):
        pass

    # Exit a parse tree produced by ParserGrammarParser#sequence.
    def exitSequence(self, ctx:ParserGrammarParser.SequenceContext):
        pass


    # Enter a parse tree produced by ParserGrammarParser#modifier.
    def enterModifier(self, ctx:ParserGrammarParser.ModifierContext):
        pass

    # Exit a parse tree produced by ParserGrammarParser#modifier.
    def exitModifier(self, ctx:ParserGrammarParser.ModifierContext):
        pass


    # Enter a parse tree produced by ParserGrammarParser#flag.
    def enterFlag(self, ctx:ParserGrammarParser.FlagContext):
        pass

    # Exit a parse tree produced by ParserGrammarParser#flag.
    def exitFlag(self, ctx:ParserGrammarParser.FlagContext):
        pass


    # Enter a parse tree produced by ParserGrammarParser#arg.
    def enterArg(self, ctx:ParserGrammarParser.ArgContext):
        pass

    # Exit a parse tree produced by ParserGrammarParser#arg.
    def exitArg(self, ctx:ParserGrammarParser.ArgContext):
        pass


    # Enter a parse tree produced by ParserGrammarParser#name.
    def enterName(self, ctx:ParserGrammarParser.NameContext):
        pass

    # Exit a parse tree produced by ParserGrammarParser#name.
    def exitName(self, ctx:ParserGrammarParser.NameContext):
        pass


    # Enter a parse tree produced by ParserGrammarParser#redirect.
    def enterRedirect(self, ctx:ParserGrammarParser.RedirectContext):
        pass

    # Exit a parse tree produced by ParserGrammarParser#redirect.
    def exitRedirect(self, ctx:ParserGrammarParser.RedirectContext):
        pass


    # Enter a parse tree produced by ParserGrammarParser#subcommand.
    def enterSubcommand(self, ctx:ParserGrammarParser.SubcommandContext):
        pass

    # Exit a parse tree produced by ParserGrammarParser#subcommand.
    def exitSubcommand(self, ctx:ParserGrammarParser.SubcommandContext):
        pass


    # Enter a parse tree produced by ParserGrammarParser#phrase.
    def enterPhrase(self, ctx:ParserGrammarParser.PhraseContext):
        pass

    # Exit a parse tree produced by ParserGrammarParser#phrase.
    def exitPhrase(self, ctx:ParserGrammarParser.PhraseContext):
        pass


    # Enter a parse tree produced by ParserGrammarParser#literal.
    def enterLiteral(self, ctx:ParserGrammarParser.LiteralContext):
        pass

    # Exit a parse tree produced by ParserGrammarParser#literal.
    def exitLiteral(self, ctx:ParserGrammarParser.LiteralContext):
        pass


    # Enter a parse tree produced by ParserGrammarParser#string.
    def enterString(self, ctx:ParserGrammarParser.StringContext):
        pass

    # Exit a parse tree produced by ParserGrammarParser#string.
    def exitString(self, ctx:ParserGrammarParser.StringContext):
        pass


    # Enter a parse tree produced by ParserGrammarParser#dq_string.
    def enterDq_string(self, ctx:ParserGrammarParser.Dq_stringContext):
        pass

    # Exit a parse tree produced by ParserGrammarParser#dq_string.
    def exitDq_string(self, ctx:ParserGrammarParser.Dq_stringContext):
        pass


    # Enter a parse tree produced by ParserGrammarParser#sq_string.
    def enterSq_string(self, ctx:ParserGrammarParser.Sq_stringContext):
        pass

    # Exit a parse tree produced by ParserGrammarParser#sq_string.
    def exitSq_string(self, ctx:ParserGrammarParser.Sq_stringContext):
        pass



del ParserGrammarParser