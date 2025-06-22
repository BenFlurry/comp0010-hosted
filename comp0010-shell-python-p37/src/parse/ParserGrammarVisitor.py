# Generated from ParserGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ParserGrammarParser import ParserGrammarParser
else:
    from ParserGrammarParser import ParserGrammarParser

# This class defines a complete generic visitor for a parse tree produced by ParserGrammarParser.

class ParserGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ParserGrammarParser#start.
    def visitStart(self, ctx:ParserGrammarParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammarParser#commandLine.
    def visitCommandLine(self, ctx:ParserGrammarParser.CommandLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammarParser#command.
    def visitCommand(self, ctx:ParserGrammarParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammarParser#pipe.
    def visitPipe(self, ctx:ParserGrammarParser.PipeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammarParser#sequence.
    def visitSequence(self, ctx:ParserGrammarParser.SequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammarParser#modifier.
    def visitModifier(self, ctx:ParserGrammarParser.ModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammarParser#flag.
    def visitFlag(self, ctx:ParserGrammarParser.FlagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammarParser#arg.
    def visitArg(self, ctx:ParserGrammarParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammarParser#name.
    def visitName(self, ctx:ParserGrammarParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammarParser#redirect.
    def visitRedirect(self, ctx:ParserGrammarParser.RedirectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammarParser#subcommand.
    def visitSubcommand(self, ctx:ParserGrammarParser.SubcommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammarParser#phrase.
    def visitPhrase(self, ctx:ParserGrammarParser.PhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammarParser#literal.
    def visitLiteral(self, ctx:ParserGrammarParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammarParser#string.
    def visitString(self, ctx:ParserGrammarParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammarParser#dq_string.
    def visitDq_string(self, ctx:ParserGrammarParser.Dq_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammarParser#sq_string.
    def visitSq_string(self, ctx:ParserGrammarParser.Sq_stringContext):
        return self.visitChildren(ctx)



del ParserGrammarParser