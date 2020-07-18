# Generated from .\DatalogGrammar.g4 by ANTLR 4.8
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .DatalogGrammarParser import DatalogGrammarParser
else:
    from DatalogGrammarParser import DatalogGrammarParser


# This class defines a complete generic visitor for a parse tree produced by DatalogGrammarParser.

class DatalogGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DatalogGrammarParser#output.
    def visitOutput(self, ctx: DatalogGrammarParser.OutputContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DatalogGrammarParser#predicate_atom.
    def visitPredicate_atom(self, ctx: DatalogGrammarParser.Predicate_atomContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DatalogGrammarParser#term.
    def visitTerm(self, ctx: DatalogGrammarParser.TermContext):
        return self.visitChildren(ctx)


del DatalogGrammarParser
