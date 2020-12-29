
from antlr4 import PredictionMode
from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.error.ErrorListener import ConsoleErrorListener
from antlr4.error.Errors import RecognitionException
from antlr4.error.ErrorStrategy import BailErrorStrategy, DefaultErrorStrategy
from antlr4.InputStream import InputStream

from .IDLVLexer import IDLVLexer
from .IDLVParser import IDLVParser
from .IDLVParserVisitor import IDLVParserVisitor


class IDLVParserVisitorImplementation(IDLVParserVisitor):
    def __init__(self, models):
        self._models = models
        self._model_currently_being_visited = None

    def visitMinimal_model(self, ctx):
        self._models.add_minimal_model()
        return self.visitChildren(ctx)

    def visitPredicate_atom(self, ctx):
        self._model_currently_being_visited.get_atoms_as_stringlist().add(ctx.getText())

    @staticmethod
    def parse(minimalModels, idlvOutput, two_stageParsing):
        tokens = CommonTokenStream(IDLVLexer(InputStream(idlvOutput)))
        parser = IDLVParser(tokens)
        visitor = IDLVParserVisitorImplementation(minimalModels)

        if not two_stageParsing:
            visitor.visit(parser.output())

            return

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
