from antlr4 import PredictionMode
from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.error.ErrorListener import ConsoleErrorListener
from antlr4.error.Errors import RecognitionException
from antlr4.error.ErrorStrategy import BailErrorStrategy, DefaultErrorStrategy
from antlr4.InputStream import InputStream

from .datalog_parser_base.DatalogGrammarLexer import DatalogGrammarLexer
from .datalog_parser_base.DatalogGrammarParser import DatalogGrammarParser
from .datalog_parser_base.DatalogGrammarVisitor import DatalogGrammarVisitor


class DatalogParser(DatalogGrammarVisitor):
    _term_list = []

    @staticmethod
    def parse_parameters_from_atom(atom):
        DatalogParser._term_list.clear()
        tokens = CommonTokenStream(DatalogGrammarLexer(InputStream(atom)))
        parser = DatalogGrammarParser(tokens)
        visitor = DatalogParser()
        parser._interp.predictionMode = PredictionMode.SLL

        parser.removeErrorListeners()

        parser._errHandler = BailErrorStrategy()

        try:
            visitor.visit(parser.output())
        except RuntimeError as exception:
            if isinstance(exception, RecognitionException):
                tokens.seek(0)
                parser.addErrorListener(ConsoleErrorListener.INSTANCE)

                parser._errHandler = DefaultErrorStrategy()
                parser._interp.predictionMode = PredictionMode.LL

                visitor.visit(parser.output())

        return DatalogParser._term_list

    def get_term_list(self):
        return self._term_list

    def visitTerm(self, ctx):
        self._term_list.append(ctx.getText())

        return None
