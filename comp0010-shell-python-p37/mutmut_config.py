# mypy: ignore-errors
"""
A config file for mutmut. Will not be tested since it exists independently of
the rest of the codebase.
"""


def pre_mutation(context):
    """
    A function to skip the parser grammar files, since they are generated and
    cannot be mutated.
    """
    files_to_skip = [
        "ParserGrammarLexer",
        "ParserGrammarListener",
        "ParserGrammarParser",
        "ParserGrammarVisitor",
        "parser_test",
    ]

    # If any of the names of the files to skip are in the file path, skip it.
    for file_to_skip in files_to_skip:
        # print("file_to_skip: ", file_to_skip)
        if file_to_skip in context.filename:
            context.skip = True


def test_command():
    """
    A function to run the tests.
    """
    return "python -m nose2 test"
