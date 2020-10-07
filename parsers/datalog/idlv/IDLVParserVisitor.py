# Generated from .\IDLVParser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .IDLVParser import IDLVParser
else:
    from IDLVParser import IDLVParser

# This class defines a complete generic visitor for a parse tree produced by IDLVParser.

class IDLVParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by IDLVParser#output.
    def visitOutput(self, ctx:IDLVParser.OutputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLVParser#minimal_model.
    def visitMinimal_model(self, ctx:IDLVParser.Minimal_modelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLVParser#predicate_atom.
    def visitPredicate_atom(self, ctx:IDLVParser.Predicate_atomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLVParser#term.
    def visitTerm(self, ctx:IDLVParser.TermContext):
        return self.visitChildren(ctx)



del IDLVParser