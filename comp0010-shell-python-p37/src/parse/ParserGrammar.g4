grammar ParserGrammar;

// ====Parser Rules====

start: commandLine? SPACE* EOF;

// Represents a complete command line, which can be a single command, a pipe, or a sequence.
commandLine: (command | pipe | sequence);

// A command is made up of a name followed by zero or more modifiers.
command: (SPACE* redirect SPACE*)* name (SPACE* redirect | SPACE modifier)*;

// A pipe is either two commands, or a pipe and a command. Pipes are always left-associative.
pipe: command SPACE? '|' SPACE? command
  | pipe SPACE? '|' SPACE? command
  ;

// A sequence is either two commands, a sequence and a command, a pipe and a command, or a pipe and a pipe.
sequence: command SPACE? ';' SPACE? command
  | sequence SPACE? ';' SPACE? command
  | pipe SPACE? ';' SPACE? command
  | pipe SPACE? ';' SPACE? pipe
  | command SPACE? ';' SPACE? pipe
  ;

modifier: redirect
  | flag
  | arg
  ;

// Using the WORD lexer accounts for -name and at the moment flags with values must have an =
flag: '-' phrase;

arg: phrase;

name: phrase;

// Represents a redirection, either input ('<') or output ('>'), followed by a word (the file path).
redirect: ('<' | '>') SPACE? phrase;

// Represents a subcommand wrapped in backticks
subcommand: '`' SPACE? commandLine? SPACE? '`';

// A phrase is any combination of a string, chars or subcommands
phrase: phrase string
  | CHARS
  | '-'
  | ('`' SPACE? '`') phrase
  | phrase ('`' SPACE? '`')
  | subcommand phrase
  | phrase subcommand
  | subcommand
  | string+
  | string phrase
  | CHARS phrase
  | '-' phrase;

// We can't add these characters in the lexer, otherwise we can't use them in the rules
// Lexers don't have inheritance rules; if LITERAL: CHARS | [-<>;|], then all defined characters are
// matched as a LITERAL. It is not useful to us in that context, and hence, we use a parser rule
// instead.
literal: CHARS | '-' | '<' | '>' | ';' | '|';

// A quoted string can contain subcommands, hence it cannot be a lexer rule
string: (dq_string | sq_string);
dq_string: '"' ('\'' | literal+ | SPACE+ | subcommand)* '"';
sq_string: '\'' ( '"' | literal+ | SPACE+ | subcommand)* '\'';

// ====Lexer Rules====

SPACE: [ \t]+;

NEWLINE: [\r\n]+ -> skip;

CHARS: (~[-"'\r\n`|;<> ] | ('\\' ('"' | '\'')))+;
