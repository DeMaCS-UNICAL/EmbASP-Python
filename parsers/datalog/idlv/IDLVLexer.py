# Generated from .\IDLVLexer.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\n")
        buf.write("G\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\5\2")
        buf.write("\34\n\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\7\6(\n")
        buf.write("\6\f\6\16\6+\13\6\3\7\3\7\7\7/\n\7\f\7\16\7\62\13\7\3")
        buf.write("\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\7\n=\n\n\f\n\16\n@")
        buf.write("\13\n\5\nB\n\n\3\13\3\13\3\f\3\f\2\2\r\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\2\25\2\27\2\3\2\t\4\2C\\c|\6\2")
        buf.write("\62;C\\aac|\3\2$$\3\2\63;\3\2\62;\4\2\f\f\17\17\4\2\13")
        buf.write("\13\"\"\2H\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\3\33\3\2\2\2\5\37\3\2\2\2\7!\3\2\2\2\t#\3\2\2\2\13")
        buf.write("%\3\2\2\2\r,\3\2\2\2\17\65\3\2\2\2\21\67\3\2\2\2\23A\3")
        buf.write("\2\2\2\25C\3\2\2\2\27E\3\2\2\2\31\34\5\25\13\2\32\34\5")
        buf.write("\27\f\2\33\31\3\2\2\2\33\32\3\2\2\2\34\35\3\2\2\2\35\36")
        buf.write("\b\2\2\2\36\4\3\2\2\2\37 \7.\2\2 \6\3\2\2\2!\"\5\23\n")
        buf.write("\2\"\b\3\2\2\2#$\7\60\2\2$\n\3\2\2\2%)\t\2\2\2&(\t\3\2")
        buf.write("\2\'&\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*\f\3\2\2")
        buf.write("\2+)\3\2\2\2,\60\7$\2\2-/\n\4\2\2.-\3\2\2\2/\62\3\2\2")
        buf.write("\2\60.\3\2\2\2\60\61\3\2\2\2\61\63\3\2\2\2\62\60\3\2\2")
        buf.write("\2\63\64\7$\2\2\64\16\3\2\2\2\65\66\7*\2\2\66\20\3\2\2")
        buf.write("\2\678\7+\2\28\22\3\2\2\29B\7\62\2\2:>\t\5\2\2;=\t\6\2")
        buf.write("\2<;\3\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2\2\2?B\3\2\2\2@")
        buf.write(">\3\2\2\2A9\3\2\2\2A:\3\2\2\2B\24\3\2\2\2CD\t\7\2\2D\26")
        buf.write("\3\2\2\2EF\t\b\2\2F\30\3\2\2\2\b\2\33)\60>A\3\b\2\2")
        return buf.getvalue()


class IDLVLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IGNORE = 1
    COMMA = 2
    INTEGER_CONSTANT = 3
    ATOM_END = 4
    IDENTIFIER = 5
    STRING_CONSTANT = 6
    TERMS_BEGIN = 7
    TERMS_END = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "'.'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "IGNORE", "COMMA", "INTEGER_CONSTANT", "ATOM_END", "IDENTIFIER", 
            "STRING_CONSTANT", "TERMS_BEGIN", "TERMS_END" ]

    ruleNames = [ "IGNORE", "COMMA", "INTEGER_CONSTANT", "ATOM_END", "IDENTIFIER", 
                  "STRING_CONSTANT", "TERMS_BEGIN", "TERMS_END", "INT", 
                  "NL", "WS" ]

    grammarFileName = "IDLVLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


