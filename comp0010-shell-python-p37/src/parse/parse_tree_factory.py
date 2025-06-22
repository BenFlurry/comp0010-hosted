"""
A generalized parser function that returns a tree
"""

from antlr4 import CommonTokenStream, InputStream  # type: ignore

from parse.ParserGrammarLexer import ParserGrammarLexer
from parse.ParserGrammarParser import ParserGrammarParser
from parse.shell_error_listener import ShellErrorListener


def create_parse_tree(cmdline: str) -> ParserGrammarParser.StartContext:
    """
    Creates a parse tree with the command line.

    Args:
        cmdline (str): A commond line to parse
    """
    # Tokenize the input
    lexer = ParserGrammarLexer(InputStream(cmdline))
    stream = CommonTokenStream(lexer)

    # Parse the tokenized input
    listener = ShellErrorListener()
    parser = ParserGrammarParser(stream)

    # Remove the default error listener
    parser.removeErrorListeners()
    parser.addErrorListener(listener)
    return parser.start()
