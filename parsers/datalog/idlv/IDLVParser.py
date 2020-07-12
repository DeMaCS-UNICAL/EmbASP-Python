# Generated from .\IDLVParser.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\n")
        buf.write("%\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\3\3\3\3\3")
        buf.write("\7\3\20\n\3\f\3\16\3\23\13\3\3\4\3\4\3\4\3\4\3\4\7\4\32")
        buf.write("\n\4\f\4\16\4\35\13\4\3\4\3\4\5\4!\n\4\3\5\3\5\3\5\2\2")
        buf.write("\6\2\4\6\b\2\3\4\2\5\5\7\b\2#\2\n\3\2\2\2\4\21\3\2\2\2")
        buf.write("\6\24\3\2\2\2\b\"\3\2\2\2\n\13\5\4\3\2\13\3\3\2\2\2\f")
        buf.write("\r\5\6\4\2\r\16\7\6\2\2\16\20\3\2\2\2\17\f\3\2\2\2\20")
        buf.write("\23\3\2\2\2\21\17\3\2\2\2\21\22\3\2\2\2\22\5\3\2\2\2\23")
        buf.write("\21\3\2\2\2\24 \7\7\2\2\25\26\7\t\2\2\26\33\5\b\5\2\27")
        buf.write("\30\7\4\2\2\30\32\5\b\5\2\31\27\3\2\2\2\32\35\3\2\2\2")
        buf.write("\33\31\3\2\2\2\33\34\3\2\2\2\34\36\3\2\2\2\35\33\3\2\2")
        buf.write("\2\36\37\7\n\2\2\37!\3\2\2\2 \25\3\2\2\2 !\3\2\2\2!\7")
        buf.write("\3\2\2\2\"#\t\2\2\2#\t\3\2\2\2\5\21\33 ")
        return buf.getvalue()


class IDLVParser ( Parser ):

    grammarFileName = "IDLVParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "','", "<INVALID>", "'.'", 
                     "<INVALID>", "<INVALID>", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "IGNORE", "COMMA", "INTEGER_CONSTANT", 
                      "ATOM_END", "IDENTIFIER", "STRING_CONSTANT", "TERMS_BEGIN", 
                      "TERMS_END" ]

    RULE_output = 0
    RULE_minimal_model = 1
    RULE_predicate_atom = 2
    RULE_term = 3

    ruleNames =  [ "output", "minimal_model", "predicate_atom", "term" ]

    EOF = Token.EOF
    IGNORE=1
    COMMA=2
    INTEGER_CONSTANT=3
    ATOM_END=4
    IDENTIFIER=5
    STRING_CONSTANT=6
    TERMS_BEGIN=7
    TERMS_END=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class OutputContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def minimal_model(self):
            return self.getTypedRuleContext(IDLVParser.Minimal_modelContext,0)


        def getRuleIndex(self):
            return IDLVParser.RULE_output

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutput" ):
                return visitor.visitOutput(self)
            else:
                return visitor.visitChildren(self)




    def output(self):

        localctx = IDLVParser.OutputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_output)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.minimal_model()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Minimal_modelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predicate_atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IDLVParser.Predicate_atomContext)
            else:
                return self.getTypedRuleContext(IDLVParser.Predicate_atomContext,i)


        def ATOM_END(self, i:int=None):
            if i is None:
                return self.getTokens(IDLVParser.ATOM_END)
            else:
                return self.getToken(IDLVParser.ATOM_END, i)

        def getRuleIndex(self):
            return IDLVParser.RULE_minimal_model

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinimal_model" ):
                return visitor.visitMinimal_model(self)
            else:
                return visitor.visitChildren(self)




    def minimal_model(self):

        localctx = IDLVParser.Minimal_modelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_minimal_model)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IDLVParser.IDENTIFIER:
                self.state = 10
                self.predicate_atom()
                self.state = 11
                self.match(IDLVParser.ATOM_END)
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Predicate_atomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(IDLVParser.IDENTIFIER, 0)

        def TERMS_BEGIN(self):
            return self.getToken(IDLVParser.TERMS_BEGIN, 0)

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IDLVParser.TermContext)
            else:
                return self.getTypedRuleContext(IDLVParser.TermContext,i)


        def TERMS_END(self):
            return self.getToken(IDLVParser.TERMS_END, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(IDLVParser.COMMA)
            else:
                return self.getToken(IDLVParser.COMMA, i)

        def getRuleIndex(self):
            return IDLVParser.RULE_predicate_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredicate_atom" ):
                return visitor.visitPredicate_atom(self)
            else:
                return visitor.visitChildren(self)




    def predicate_atom(self):

        localctx = IDLVParser.Predicate_atomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_predicate_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(IDLVParser.IDENTIFIER)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IDLVParser.TERMS_BEGIN:
                self.state = 19
                self.match(IDLVParser.TERMS_BEGIN)
                self.state = 20
                self.term()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==IDLVParser.COMMA:
                    self.state = 21
                    self.match(IDLVParser.COMMA)
                    self.state = 22
                    self.term()
                    self.state = 27
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 28
                self.match(IDLVParser.TERMS_END)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(IDLVParser.IDENTIFIER, 0)

        def INTEGER_CONSTANT(self):
            return self.getToken(IDLVParser.INTEGER_CONSTANT, 0)

        def STRING_CONSTANT(self):
            return self.getToken(IDLVParser.STRING_CONSTANT, 0)

        def getRuleIndex(self):
            return IDLVParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = IDLVParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IDLVParser.INTEGER_CONSTANT) | (1 << IDLVParser.IDENTIFIER) | (1 << IDLVParser.STRING_CONSTANT))) != 0)):
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





