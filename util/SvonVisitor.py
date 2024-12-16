# Generated from Svon.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SvonParser import SvonParser
else:
    from SvonParser import SvonParser

# This class defines a complete generic visitor for a parse tree produced by SvonParser.

class SvonVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SvonParser#program.
    def visitProgram(self, ctx:SvonParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SvonParser#statement.
    def visitStatement(self, ctx:SvonParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SvonParser#printStatement.
    def visitPrintStatement(self, ctx:SvonParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SvonParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:SvonParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SvonParser#ifStatement.
    def visitIfStatement(self, ctx:SvonParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SvonParser#elifStatement.
    def visitElifStatement(self, ctx:SvonParser.ElifStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SvonParser#elseStatement.
    def visitElseStatement(self, ctx:SvonParser.ElseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SvonParser#forStatement.
    def visitForStatement(self, ctx:SvonParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SvonParser#whileStatement.
    def visitWhileStatement(self, ctx:SvonParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SvonParser#stringExpr.
    def visitStringExpr(self, ctx:SvonParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SvonParser#notExpr.
    def visitNotExpr(self, ctx:SvonParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SvonParser#addSubExpr.
    def visitAddSubExpr(self, ctx:SvonParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SvonParser#numberExpr.
    def visitNumberExpr(self, ctx:SvonParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SvonParser#logicalExpr.
    def visitLogicalExpr(self, ctx:SvonParser.LogicalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SvonParser#comparisonExpr.
    def visitComparisonExpr(self, ctx:SvonParser.ComparisonExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SvonParser#mulDivExpr.
    def visitMulDivExpr(self, ctx:SvonParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SvonParser#parenExpr.
    def visitParenExpr(self, ctx:SvonParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SvonParser#idExpr.
    def visitIdExpr(self, ctx:SvonParser.IdExprContext):
        return self.visitChildren(ctx)



del SvonParser