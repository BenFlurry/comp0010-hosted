# Generated from ParserGrammar.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,11,283,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,3,0,34,8,0,1,0,5,0,37,8,0,10,0,12,0,40,9,
        0,1,0,1,0,1,1,1,1,1,1,3,1,47,8,1,1,2,5,2,50,8,2,10,2,12,2,53,9,2,
        1,2,1,2,5,2,57,8,2,10,2,12,2,60,9,2,5,2,62,8,2,10,2,12,2,65,9,2,
        1,2,1,2,5,2,69,8,2,10,2,12,2,72,9,2,1,2,1,2,1,2,5,2,77,8,2,10,2,
        12,2,80,9,2,1,3,1,3,1,3,3,3,85,8,3,1,3,1,3,3,3,89,8,3,1,3,1,3,1,
        3,1,3,3,3,95,8,3,1,3,1,3,3,3,99,8,3,1,3,5,3,102,8,3,10,3,12,3,105,
        9,3,1,4,1,4,1,4,3,4,110,8,4,1,4,1,4,3,4,114,8,4,1,4,1,4,1,4,1,4,
        3,4,120,8,4,1,4,1,4,3,4,124,8,4,1,4,1,4,1,4,1,4,3,4,130,8,4,1,4,
        1,4,3,4,134,8,4,1,4,1,4,1,4,1,4,3,4,140,8,4,1,4,1,4,3,4,144,8,4,
        1,4,1,4,3,4,148,8,4,1,4,1,4,3,4,152,8,4,1,4,1,4,3,4,156,8,4,1,4,
        5,4,159,8,4,10,4,12,4,162,9,4,1,5,1,5,1,5,3,5,167,8,5,1,6,1,6,1,
        6,1,7,1,7,1,8,1,8,1,9,1,9,3,9,178,8,9,1,9,1,9,1,10,1,10,3,10,184,
        8,10,1,10,3,10,187,8,10,1,10,3,10,190,8,10,1,10,1,10,1,11,1,11,1,
        11,1,11,1,11,3,11,199,8,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,4,11,209,8,11,11,11,12,11,210,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,3,11,220,8,11,1,11,1,11,1,11,1,11,1,11,3,11,227,8,11,1,11,1,11,
        1,11,5,11,232,8,11,10,11,12,11,235,9,11,1,12,1,12,1,13,1,13,3,13,
        241,8,13,1,14,1,14,1,14,4,14,246,8,14,11,14,12,14,247,1,14,4,14,
        251,8,14,11,14,12,14,252,1,14,5,14,256,8,14,10,14,12,14,259,9,14,
        1,14,1,14,1,15,1,15,1,15,4,15,266,8,15,11,15,12,15,267,1,15,4,15,
        271,8,15,11,15,12,15,272,1,15,5,15,276,8,15,10,15,12,15,279,9,15,
        1,15,1,15,1,15,0,3,6,8,22,16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,0,2,1,0,4,5,2,0,1,5,11,11,328,0,33,1,0,0,0,2,46,1,0,0,0,4,
        63,1,0,0,0,6,81,1,0,0,0,8,147,1,0,0,0,10,166,1,0,0,0,12,168,1,0,
        0,0,14,171,1,0,0,0,16,173,1,0,0,0,18,175,1,0,0,0,20,181,1,0,0,0,
        22,219,1,0,0,0,24,236,1,0,0,0,26,240,1,0,0,0,28,242,1,0,0,0,30,262,
        1,0,0,0,32,34,3,2,1,0,33,32,1,0,0,0,33,34,1,0,0,0,34,38,1,0,0,0,
        35,37,5,9,0,0,36,35,1,0,0,0,37,40,1,0,0,0,38,36,1,0,0,0,38,39,1,
        0,0,0,39,41,1,0,0,0,40,38,1,0,0,0,41,42,5,0,0,1,42,1,1,0,0,0,43,
        47,3,4,2,0,44,47,3,6,3,0,45,47,3,8,4,0,46,43,1,0,0,0,46,44,1,0,0,
        0,46,45,1,0,0,0,47,3,1,0,0,0,48,50,5,9,0,0,49,48,1,0,0,0,50,53,1,
        0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,54,1,0,0,0,53,51,1,0,0,0,54,
        58,3,18,9,0,55,57,5,9,0,0,56,55,1,0,0,0,57,60,1,0,0,0,58,56,1,0,
        0,0,58,59,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,61,51,1,0,0,0,62,65,
        1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,66,1,0,0,0,65,63,1,0,0,0,
        66,78,3,16,8,0,67,69,5,9,0,0,68,67,1,0,0,0,69,72,1,0,0,0,70,68,1,
        0,0,0,70,71,1,0,0,0,71,73,1,0,0,0,72,70,1,0,0,0,73,77,3,18,9,0,74,
        75,5,9,0,0,75,77,3,10,5,0,76,70,1,0,0,0,76,74,1,0,0,0,77,80,1,0,
        0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,5,1,0,0,0,80,78,1,0,0,0,81,82,
        6,3,-1,0,82,84,3,4,2,0,83,85,5,9,0,0,84,83,1,0,0,0,84,85,1,0,0,0,
        85,86,1,0,0,0,86,88,5,1,0,0,87,89,5,9,0,0,88,87,1,0,0,0,88,89,1,
        0,0,0,89,90,1,0,0,0,90,91,3,4,2,0,91,103,1,0,0,0,92,94,10,1,0,0,
        93,95,5,9,0,0,94,93,1,0,0,0,94,95,1,0,0,0,95,96,1,0,0,0,96,98,5,
        1,0,0,97,99,5,9,0,0,98,97,1,0,0,0,98,99,1,0,0,0,99,100,1,0,0,0,100,
        102,3,4,2,0,101,92,1,0,0,0,102,105,1,0,0,0,103,101,1,0,0,0,103,104,
        1,0,0,0,104,7,1,0,0,0,105,103,1,0,0,0,106,107,6,4,-1,0,107,109,3,
        4,2,0,108,110,5,9,0,0,109,108,1,0,0,0,109,110,1,0,0,0,110,111,1,
        0,0,0,111,113,5,2,0,0,112,114,5,9,0,0,113,112,1,0,0,0,113,114,1,
        0,0,0,114,115,1,0,0,0,115,116,3,4,2,0,116,148,1,0,0,0,117,119,3,
        6,3,0,118,120,5,9,0,0,119,118,1,0,0,0,119,120,1,0,0,0,120,121,1,
        0,0,0,121,123,5,2,0,0,122,124,5,9,0,0,123,122,1,0,0,0,123,124,1,
        0,0,0,124,125,1,0,0,0,125,126,3,4,2,0,126,148,1,0,0,0,127,129,3,
        6,3,0,128,130,5,9,0,0,129,128,1,0,0,0,129,130,1,0,0,0,130,131,1,
        0,0,0,131,133,5,2,0,0,132,134,5,9,0,0,133,132,1,0,0,0,133,134,1,
        0,0,0,134,135,1,0,0,0,135,136,3,6,3,0,136,148,1,0,0,0,137,139,3,
        4,2,0,138,140,5,9,0,0,139,138,1,0,0,0,139,140,1,0,0,0,140,141,1,
        0,0,0,141,143,5,2,0,0,142,144,5,9,0,0,143,142,1,0,0,0,143,144,1,
        0,0,0,144,145,1,0,0,0,145,146,3,6,3,0,146,148,1,0,0,0,147,106,1,
        0,0,0,147,117,1,0,0,0,147,127,1,0,0,0,147,137,1,0,0,0,148,160,1,
        0,0,0,149,151,10,4,0,0,150,152,5,9,0,0,151,150,1,0,0,0,151,152,1,
        0,0,0,152,153,1,0,0,0,153,155,5,2,0,0,154,156,5,9,0,0,155,154,1,
        0,0,0,155,156,1,0,0,0,156,157,1,0,0,0,157,159,3,4,2,0,158,149,1,
        0,0,0,159,162,1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,9,1,0,
        0,0,162,160,1,0,0,0,163,167,3,18,9,0,164,167,3,12,6,0,165,167,3,
        14,7,0,166,163,1,0,0,0,166,164,1,0,0,0,166,165,1,0,0,0,167,11,1,
        0,0,0,168,169,5,3,0,0,169,170,3,22,11,0,170,13,1,0,0,0,171,172,3,
        22,11,0,172,15,1,0,0,0,173,174,3,22,11,0,174,17,1,0,0,0,175,177,
        7,0,0,0,176,178,5,9,0,0,177,176,1,0,0,0,177,178,1,0,0,0,178,179,
        1,0,0,0,179,180,3,22,11,0,180,19,1,0,0,0,181,183,5,6,0,0,182,184,
        5,9,0,0,183,182,1,0,0,0,183,184,1,0,0,0,184,186,1,0,0,0,185,187,
        3,2,1,0,186,185,1,0,0,0,186,187,1,0,0,0,187,189,1,0,0,0,188,190,
        5,9,0,0,189,188,1,0,0,0,189,190,1,0,0,0,190,191,1,0,0,0,191,192,
        5,6,0,0,192,21,1,0,0,0,193,194,6,11,-1,0,194,220,5,11,0,0,195,220,
        5,3,0,0,196,198,5,6,0,0,197,199,5,9,0,0,198,197,1,0,0,0,198,199,
        1,0,0,0,199,200,1,0,0,0,200,201,5,6,0,0,201,202,1,0,0,0,202,220,
        3,22,11,9,203,204,3,20,10,0,204,205,3,22,11,7,205,220,1,0,0,0,206,
        220,3,20,10,0,207,209,3,26,13,0,208,207,1,0,0,0,209,210,1,0,0,0,
        210,208,1,0,0,0,210,211,1,0,0,0,211,220,1,0,0,0,212,213,3,26,13,
        0,213,214,3,22,11,3,214,220,1,0,0,0,215,216,5,11,0,0,216,220,3,22,
        11,2,217,218,5,3,0,0,218,220,3,22,11,1,219,193,1,0,0,0,219,195,1,
        0,0,0,219,196,1,0,0,0,219,203,1,0,0,0,219,206,1,0,0,0,219,208,1,
        0,0,0,219,212,1,0,0,0,219,215,1,0,0,0,219,217,1,0,0,0,220,233,1,
        0,0,0,221,222,10,12,0,0,222,232,3,26,13,0,223,224,10,8,0,0,224,226,
        5,6,0,0,225,227,5,9,0,0,226,225,1,0,0,0,226,227,1,0,0,0,227,228,
        1,0,0,0,228,232,5,6,0,0,229,230,10,6,0,0,230,232,3,20,10,0,231,221,
        1,0,0,0,231,223,1,0,0,0,231,229,1,0,0,0,232,235,1,0,0,0,233,231,
        1,0,0,0,233,234,1,0,0,0,234,23,1,0,0,0,235,233,1,0,0,0,236,237,7,
        1,0,0,237,25,1,0,0,0,238,241,3,28,14,0,239,241,3,30,15,0,240,238,
        1,0,0,0,240,239,1,0,0,0,241,27,1,0,0,0,242,257,5,7,0,0,243,256,5,
        8,0,0,244,246,3,24,12,0,245,244,1,0,0,0,246,247,1,0,0,0,247,245,
        1,0,0,0,247,248,1,0,0,0,248,256,1,0,0,0,249,251,5,9,0,0,250,249,
        1,0,0,0,251,252,1,0,0,0,252,250,1,0,0,0,252,253,1,0,0,0,253,256,
        1,0,0,0,254,256,3,20,10,0,255,243,1,0,0,0,255,245,1,0,0,0,255,250,
        1,0,0,0,255,254,1,0,0,0,256,259,1,0,0,0,257,255,1,0,0,0,257,258,
        1,0,0,0,258,260,1,0,0,0,259,257,1,0,0,0,260,261,5,7,0,0,261,29,1,
        0,0,0,262,277,5,8,0,0,263,276,5,7,0,0,264,266,3,24,12,0,265,264,
        1,0,0,0,266,267,1,0,0,0,267,265,1,0,0,0,267,268,1,0,0,0,268,276,
        1,0,0,0,269,271,5,9,0,0,270,269,1,0,0,0,271,272,1,0,0,0,272,270,
        1,0,0,0,272,273,1,0,0,0,273,276,1,0,0,0,274,276,3,20,10,0,275,263,
        1,0,0,0,275,265,1,0,0,0,275,270,1,0,0,0,275,274,1,0,0,0,276,279,
        1,0,0,0,277,275,1,0,0,0,277,278,1,0,0,0,278,280,1,0,0,0,279,277,
        1,0,0,0,280,281,5,8,0,0,281,31,1,0,0,0,46,33,38,46,51,58,63,70,76,
        78,84,88,94,98,103,109,113,119,123,129,133,139,143,147,151,155,160,
        166,177,183,186,189,198,210,219,226,231,233,240,247,252,255,257,
        267,272,275,277
    ]

class ParserGrammarParser ( Parser ):

    grammarFileName = "ParserGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'|'", "';'", "'-'", "'<'", "'>'", "'`'", 
                     "'\"'", "'''" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "SPACE", "NEWLINE", "CHARS" ]

    RULE_start = 0
    RULE_commandLine = 1
    RULE_command = 2
    RULE_pipe = 3
    RULE_sequence = 4
    RULE_modifier = 5
    RULE_flag = 6
    RULE_arg = 7
    RULE_name = 8
    RULE_redirect = 9
    RULE_subcommand = 10
    RULE_phrase = 11
    RULE_literal = 12
    RULE_string = 13
    RULE_dq_string = 14
    RULE_sq_string = 15

    ruleNames =  [ "start", "commandLine", "command", "pipe", "sequence", 
                   "modifier", "flag", "arg", "name", "redirect", "subcommand", 
                   "phrase", "literal", "string", "dq_string", "sq_string" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    SPACE=9
    NEWLINE=10
    CHARS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ParserGrammarParser.EOF, 0)

        def commandLine(self):
            return self.getTypedRuleContext(ParserGrammarParser.CommandLineContext,0)


        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ParserGrammarParser.SPACE)
            else:
                return self.getToken(ParserGrammarParser.SPACE, i)

        def getRuleIndex(self):
            return ParserGrammarParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = ParserGrammarParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 32
                self.commandLine()


            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 35
                self.match(ParserGrammarParser.SPACE)
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 41
            self.match(ParserGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self):
            return self.getTypedRuleContext(ParserGrammarParser.CommandContext,0)


        def pipe(self):
            return self.getTypedRuleContext(ParserGrammarParser.PipeContext,0)


        def sequence(self):
            return self.getTypedRuleContext(ParserGrammarParser.SequenceContext,0)


        def getRuleIndex(self):
            return ParserGrammarParser.RULE_commandLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommandLine" ):
                listener.enterCommandLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommandLine" ):
                listener.exitCommandLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommandLine" ):
                return visitor.visitCommandLine(self)
            else:
                return visitor.visitChildren(self)




    def commandLine(self):

        localctx = ParserGrammarParser.CommandLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_commandLine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 43
                self.command()
                pass

            elif la_ == 2:
                self.state = 44
                self.pipe(0)
                pass

            elif la_ == 3:
                self.state = 45
                self.sequence(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(ParserGrammarParser.NameContext,0)


        def redirect(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserGrammarParser.RedirectContext)
            else:
                return self.getTypedRuleContext(ParserGrammarParser.RedirectContext,i)


        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ParserGrammarParser.SPACE)
            else:
                return self.getToken(ParserGrammarParser.SPACE, i)

        def modifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserGrammarParser.ModifierContext)
            else:
                return self.getTypedRuleContext(ParserGrammarParser.ModifierContext,i)


        def getRuleIndex(self):
            return ParserGrammarParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = ParserGrammarParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 560) != 0):
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 48
                    self.match(ParserGrammarParser.SPACE)
                    self.state = 53
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 54
                self.redirect()
                self.state = 58
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 55
                        self.match(ParserGrammarParser.SPACE) 
                    self.state = 60
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.name()
            self.state = 78
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 76
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        self.state = 70
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==9:
                            self.state = 67
                            self.match(ParserGrammarParser.SPACE)
                            self.state = 72
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 73
                        self.redirect()
                        pass

                    elif la_ == 2:
                        self.state = 74
                        self.match(ParserGrammarParser.SPACE)
                        self.state = 75
                        self.modifier()
                        pass

             
                self.state = 80
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PipeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserGrammarParser.CommandContext)
            else:
                return self.getTypedRuleContext(ParserGrammarParser.CommandContext,i)


        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ParserGrammarParser.SPACE)
            else:
                return self.getToken(ParserGrammarParser.SPACE, i)

        def pipe(self):
            return self.getTypedRuleContext(ParserGrammarParser.PipeContext,0)


        def getRuleIndex(self):
            return ParserGrammarParser.RULE_pipe

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPipe" ):
                listener.enterPipe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPipe" ):
                listener.exitPipe(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPipe" ):
                return visitor.visitPipe(self)
            else:
                return visitor.visitChildren(self)



    def pipe(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ParserGrammarParser.PipeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_pipe, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.command()
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 83
                self.match(ParserGrammarParser.SPACE)


            self.state = 86
            self.match(ParserGrammarParser.T__0)
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 87
                self.match(ParserGrammarParser.SPACE)


            self.state = 90
            self.command()
            self._ctx.stop = self._input.LT(-1)
            self.state = 103
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ParserGrammarParser.PipeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_pipe)
                    self.state = 92
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 94
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==9:
                        self.state = 93
                        self.match(ParserGrammarParser.SPACE)


                    self.state = 96
                    self.match(ParserGrammarParser.T__0)
                    self.state = 98
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        self.state = 97
                        self.match(ParserGrammarParser.SPACE)


                    self.state = 100
                    self.command() 
                self.state = 105
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class SequenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserGrammarParser.CommandContext)
            else:
                return self.getTypedRuleContext(ParserGrammarParser.CommandContext,i)


        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ParserGrammarParser.SPACE)
            else:
                return self.getToken(ParserGrammarParser.SPACE, i)

        def pipe(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserGrammarParser.PipeContext)
            else:
                return self.getTypedRuleContext(ParserGrammarParser.PipeContext,i)


        def sequence(self):
            return self.getTypedRuleContext(ParserGrammarParser.SequenceContext,0)


        def getRuleIndex(self):
            return ParserGrammarParser.RULE_sequence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequence" ):
                listener.enterSequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequence" ):
                listener.exitSequence(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequence" ):
                return visitor.visitSequence(self)
            else:
                return visitor.visitChildren(self)



    def sequence(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ParserGrammarParser.SequenceContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_sequence, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 107
                self.command()
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 108
                    self.match(ParserGrammarParser.SPACE)


                self.state = 111
                self.match(ParserGrammarParser.T__1)
                self.state = 113
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 112
                    self.match(ParserGrammarParser.SPACE)


                self.state = 115
                self.command()
                pass

            elif la_ == 2:
                self.state = 117
                self.pipe(0)
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 118
                    self.match(ParserGrammarParser.SPACE)


                self.state = 121
                self.match(ParserGrammarParser.T__1)
                self.state = 123
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 122
                    self.match(ParserGrammarParser.SPACE)


                self.state = 125
                self.command()
                pass

            elif la_ == 3:
                self.state = 127
                self.pipe(0)
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 128
                    self.match(ParserGrammarParser.SPACE)


                self.state = 131
                self.match(ParserGrammarParser.T__1)
                self.state = 133
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 132
                    self.match(ParserGrammarParser.SPACE)


                self.state = 135
                self.pipe(0)
                pass

            elif la_ == 4:
                self.state = 137
                self.command()
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 138
                    self.match(ParserGrammarParser.SPACE)


                self.state = 141
                self.match(ParserGrammarParser.T__1)
                self.state = 143
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 142
                    self.match(ParserGrammarParser.SPACE)


                self.state = 145
                self.pipe(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 160
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ParserGrammarParser.SequenceContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_sequence)
                    self.state = 149
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 151
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==9:
                        self.state = 150
                        self.match(ParserGrammarParser.SPACE)


                    self.state = 153
                    self.match(ParserGrammarParser.T__1)
                    self.state = 155
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        self.state = 154
                        self.match(ParserGrammarParser.SPACE)


                    self.state = 157
                    self.command() 
                self.state = 162
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def redirect(self):
            return self.getTypedRuleContext(ParserGrammarParser.RedirectContext,0)


        def flag(self):
            return self.getTypedRuleContext(ParserGrammarParser.FlagContext,0)


        def arg(self):
            return self.getTypedRuleContext(ParserGrammarParser.ArgContext,0)


        def getRuleIndex(self):
            return ParserGrammarParser.RULE_modifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModifier" ):
                listener.enterModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModifier" ):
                listener.exitModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModifier" ):
                return visitor.visitModifier(self)
            else:
                return visitor.visitChildren(self)




    def modifier(self):

        localctx = ParserGrammarParser.ModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_modifier)
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.redirect()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.flag()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 165
                self.arg()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FlagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def phrase(self):
            return self.getTypedRuleContext(ParserGrammarParser.PhraseContext,0)


        def getRuleIndex(self):
            return ParserGrammarParser.RULE_flag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFlag" ):
                listener.enterFlag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFlag" ):
                listener.exitFlag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFlag" ):
                return visitor.visitFlag(self)
            else:
                return visitor.visitChildren(self)




    def flag(self):

        localctx = ParserGrammarParser.FlagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_flag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(ParserGrammarParser.T__2)
            self.state = 169
            self.phrase(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def phrase(self):
            return self.getTypedRuleContext(ParserGrammarParser.PhraseContext,0)


        def getRuleIndex(self):
            return ParserGrammarParser.RULE_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg" ):
                listener.enterArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg" ):
                listener.exitArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg" ):
                return visitor.visitArg(self)
            else:
                return visitor.visitChildren(self)




    def arg(self):

        localctx = ParserGrammarParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.phrase(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def phrase(self):
            return self.getTypedRuleContext(ParserGrammarParser.PhraseContext,0)


        def getRuleIndex(self):
            return ParserGrammarParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = ParserGrammarParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.phrase(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RedirectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def phrase(self):
            return self.getTypedRuleContext(ParserGrammarParser.PhraseContext,0)


        def SPACE(self):
            return self.getToken(ParserGrammarParser.SPACE, 0)

        def getRuleIndex(self):
            return ParserGrammarParser.RULE_redirect

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRedirect" ):
                listener.enterRedirect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRedirect" ):
                listener.exitRedirect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRedirect" ):
                return visitor.visitRedirect(self)
            else:
                return visitor.visitChildren(self)




    def redirect(self):

        localctx = ParserGrammarParser.RedirectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_redirect)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 176
                self.match(ParserGrammarParser.SPACE)


            self.state = 179
            self.phrase(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubcommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ParserGrammarParser.SPACE)
            else:
                return self.getToken(ParserGrammarParser.SPACE, i)

        def commandLine(self):
            return self.getTypedRuleContext(ParserGrammarParser.CommandLineContext,0)


        def getRuleIndex(self):
            return ParserGrammarParser.RULE_subcommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubcommand" ):
                listener.enterSubcommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubcommand" ):
                listener.exitSubcommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubcommand" ):
                return visitor.visitSubcommand(self)
            else:
                return visitor.visitChildren(self)




    def subcommand(self):

        localctx = ParserGrammarParser.SubcommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_subcommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(ParserGrammarParser.T__5)
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 182
                self.match(ParserGrammarParser.SPACE)


            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 185
                self.commandLine()


            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 188
                self.match(ParserGrammarParser.SPACE)


            self.state = 191
            self.match(ParserGrammarParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PhraseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHARS(self):
            return self.getToken(ParserGrammarParser.CHARS, 0)

        def phrase(self):
            return self.getTypedRuleContext(ParserGrammarParser.PhraseContext,0)


        def SPACE(self):
            return self.getToken(ParserGrammarParser.SPACE, 0)

        def subcommand(self):
            return self.getTypedRuleContext(ParserGrammarParser.SubcommandContext,0)


        def string(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserGrammarParser.StringContext)
            else:
                return self.getTypedRuleContext(ParserGrammarParser.StringContext,i)


        def getRuleIndex(self):
            return ParserGrammarParser.RULE_phrase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPhrase" ):
                listener.enterPhrase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPhrase" ):
                listener.exitPhrase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPhrase" ):
                return visitor.visitPhrase(self)
            else:
                return visitor.visitChildren(self)



    def phrase(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ParserGrammarParser.PhraseContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_phrase, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 194
                self.match(ParserGrammarParser.CHARS)
                pass

            elif la_ == 2:
                self.state = 195
                self.match(ParserGrammarParser.T__2)
                pass

            elif la_ == 3:
                self.state = 196
                self.match(ParserGrammarParser.T__5)
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 197
                    self.match(ParserGrammarParser.SPACE)


                self.state = 200
                self.match(ParserGrammarParser.T__5)
                self.state = 202
                self.phrase(9)
                pass

            elif la_ == 4:
                self.state = 203
                self.subcommand()
                self.state = 204
                self.phrase(7)
                pass

            elif la_ == 5:
                self.state = 206
                self.subcommand()
                pass

            elif la_ == 6:
                self.state = 208 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 207
                        self.string()

                    else:
                        raise NoViableAltException(self)
                    self.state = 210 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

                pass

            elif la_ == 7:
                self.state = 212
                self.string()
                self.state = 213
                self.phrase(3)
                pass

            elif la_ == 8:
                self.state = 215
                self.match(ParserGrammarParser.CHARS)
                self.state = 216
                self.phrase(2)
                pass

            elif la_ == 9:
                self.state = 217
                self.match(ParserGrammarParser.T__2)
                self.state = 218
                self.phrase(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 233
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 231
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        localctx = ParserGrammarParser.PhraseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_phrase)
                        self.state = 221
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 222
                        self.string()
                        pass

                    elif la_ == 2:
                        localctx = ParserGrammarParser.PhraseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_phrase)
                        self.state = 223
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")

                        self.state = 224
                        self.match(ParserGrammarParser.T__5)
                        self.state = 226
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==9:
                            self.state = 225
                            self.match(ParserGrammarParser.SPACE)


                        self.state = 228
                        self.match(ParserGrammarParser.T__5)
                        pass

                    elif la_ == 3:
                        localctx = ParserGrammarParser.PhraseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_phrase)
                        self.state = 229
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 230
                        self.subcommand()
                        pass

             
                self.state = 235
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHARS(self):
            return self.getToken(ParserGrammarParser.CHARS, 0)

        def getRuleIndex(self):
            return ParserGrammarParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ParserGrammarParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2110) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dq_string(self):
            return self.getTypedRuleContext(ParserGrammarParser.Dq_stringContext,0)


        def sq_string(self):
            return self.getTypedRuleContext(ParserGrammarParser.Sq_stringContext,0)


        def getRuleIndex(self):
            return ParserGrammarParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = ParserGrammarParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.state = 238
                self.dq_string()
                pass
            elif token in [8]:
                self.state = 239
                self.sq_string()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dq_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subcommand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserGrammarParser.SubcommandContext)
            else:
                return self.getTypedRuleContext(ParserGrammarParser.SubcommandContext,i)


        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserGrammarParser.LiteralContext)
            else:
                return self.getTypedRuleContext(ParserGrammarParser.LiteralContext,i)


        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ParserGrammarParser.SPACE)
            else:
                return self.getToken(ParserGrammarParser.SPACE, i)

        def getRuleIndex(self):
            return ParserGrammarParser.RULE_dq_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDq_string" ):
                listener.enterDq_string(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDq_string" ):
                listener.exitDq_string(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDq_string" ):
                return visitor.visitDq_string(self)
            else:
                return visitor.visitChildren(self)




    def dq_string(self):

        localctx = ParserGrammarParser.Dq_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_dq_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(ParserGrammarParser.T__6)
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2942) != 0):
                self.state = 255
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8]:
                    self.state = 243
                    self.match(ParserGrammarParser.T__7)
                    pass
                elif token in [1, 2, 3, 4, 5, 11]:
                    self.state = 245 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 244
                            self.literal()

                        else:
                            raise NoViableAltException(self)
                        self.state = 247 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

                    pass
                elif token in [9]:
                    self.state = 250 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 249
                            self.match(ParserGrammarParser.SPACE)

                        else:
                            raise NoViableAltException(self)
                        self.state = 252 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

                    pass
                elif token in [6]:
                    self.state = 254
                    self.subcommand()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 260
            self.match(ParserGrammarParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sq_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subcommand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserGrammarParser.SubcommandContext)
            else:
                return self.getTypedRuleContext(ParserGrammarParser.SubcommandContext,i)


        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserGrammarParser.LiteralContext)
            else:
                return self.getTypedRuleContext(ParserGrammarParser.LiteralContext,i)


        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ParserGrammarParser.SPACE)
            else:
                return self.getToken(ParserGrammarParser.SPACE, i)

        def getRuleIndex(self):
            return ParserGrammarParser.RULE_sq_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSq_string" ):
                listener.enterSq_string(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSq_string" ):
                listener.exitSq_string(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSq_string" ):
                return visitor.visitSq_string(self)
            else:
                return visitor.visitChildren(self)




    def sq_string(self):

        localctx = ParserGrammarParser.Sq_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_sq_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(ParserGrammarParser.T__7)
            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2814) != 0):
                self.state = 275
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [7]:
                    self.state = 263
                    self.match(ParserGrammarParser.T__6)
                    pass
                elif token in [1, 2, 3, 4, 5, 11]:
                    self.state = 265 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 264
                            self.literal()

                        else:
                            raise NoViableAltException(self)
                        self.state = 267 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

                    pass
                elif token in [9]:
                    self.state = 270 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 269
                            self.match(ParserGrammarParser.SPACE)

                        else:
                            raise NoViableAltException(self)
                        self.state = 272 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

                    pass
                elif token in [6]:
                    self.state = 274
                    self.subcommand()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 279
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 280
            self.match(ParserGrammarParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.pipe_sempred
        self._predicates[4] = self.sequence_sempred
        self._predicates[11] = self.phrase_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def pipe_sempred(self, localctx:PipeContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def sequence_sempred(self, localctx:SequenceContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

    def phrase_sempred(self, localctx:PhraseContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         




