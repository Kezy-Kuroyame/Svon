# Generated from Svon.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SvonParser import SvonParser
else:
    from SvonParser import SvonParser

# This class defines a complete listener for a parse tree produced by SvonParser.
class SvonListener(ParseTreeListener):

    # Enter a parse tree produced by SvonParser#program.
    def enterProgram(self, ctx:SvonParser.ProgramContext):
        pass

    # Exit a parse tree produced by SvonParser#program.
    def exitProgram(self, ctx:SvonParser.ProgramContext):
        pass


    # Enter a parse tree produced by SvonParser#statement.
    def enterStatement(self, ctx:SvonParser.StatementContext):
        pass

    # Exit a parse tree produced by SvonParser#statement.
    def exitStatement(self, ctx:SvonParser.StatementContext):
        pass


    # Enter a parse tree produced by SvonParser#printStatement.
    def enterPrintStatement(self, ctx:SvonParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by SvonParser#printStatement.
    def exitPrintStatement(self, ctx:SvonParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by SvonParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:SvonParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by SvonParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:SvonParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by SvonParser#ifStatement.
    def enterIfStatement(self, ctx:SvonParser.IfStatementContext):
        pass

    # Exit a parse tree produced by SvonParser#ifStatement.
    def exitIfStatement(self, ctx:SvonParser.IfStatementContext):
        pass


    # Enter a parse tree produced by SvonParser#elifStatement.
    def enterElifStatement(self, ctx:SvonParser.ElifStatementContext):
        pass

    # Exit a parse tree produced by SvonParser#elifStatement.
    def exitElifStatement(self, ctx:SvonParser.ElifStatementContext):
        pass


    # Enter a parse tree produced by SvonParser#elseStatement.
    def enterElseStatement(self, ctx:SvonParser.ElseStatementContext):
        pass

    # Exit a parse tree produced by SvonParser#elseStatement.
    def exitElseStatement(self, ctx:SvonParser.ElseStatementContext):
        pass


    # Enter a parse tree produced by SvonParser#forStatement.
    def enterForStatement(self, ctx:SvonParser.ForStatementContext):
        pass

    # Exit a parse tree produced by SvonParser#forStatement.
    def exitForStatement(self, ctx:SvonParser.ForStatementContext):
        pass


    # Enter a parse tree produced by SvonParser#whileStatement.
    def enterWhileStatement(self, ctx:SvonParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by SvonParser#whileStatement.
    def exitWhileStatement(self, ctx:SvonParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by SvonParser#stringExpr.
    def enterStringExpr(self, ctx:SvonParser.StringExprContext):
        pass

    # Exit a parse tree produced by SvonParser#stringExpr.
    def exitStringExpr(self, ctx:SvonParser.StringExprContext):
        pass


    # Enter a parse tree produced by SvonParser#notExpr.
    def enterNotExpr(self, ctx:SvonParser.NotExprContext):
        pass

    # Exit a parse tree produced by SvonParser#notExpr.
    def exitNotExpr(self, ctx:SvonParser.NotExprContext):
        pass


    # Enter a parse tree produced by SvonParser#addSubExpr.
    def enterAddSubExpr(self, ctx:SvonParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by SvonParser#addSubExpr.
    def exitAddSubExpr(self, ctx:SvonParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by SvonParser#numberExpr.
    def enterNumberExpr(self, ctx:SvonParser.NumberExprContext):
        pass

    # Exit a parse tree produced by SvonParser#numberExpr.
    def exitNumberExpr(self, ctx:SvonParser.NumberExprContext):
        pass


    # Enter a parse tree produced by SvonParser#logicalExpr.
    def enterLogicalExpr(self, ctx:SvonParser.LogicalExprContext):
        pass

    # Exit a parse tree produced by SvonParser#logicalExpr.
    def exitLogicalExpr(self, ctx:SvonParser.LogicalExprContext):
        pass


    # Enter a parse tree produced by SvonParser#comparisonExpr.
    def enterComparisonExpr(self, ctx:SvonParser.ComparisonExprContext):
        pass

    # Exit a parse tree produced by SvonParser#comparisonExpr.
    def exitComparisonExpr(self, ctx:SvonParser.ComparisonExprContext):
        pass


    # Enter a parse tree produced by SvonParser#mulDivExpr.
    def enterMulDivExpr(self, ctx:SvonParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by SvonParser#mulDivExpr.
    def exitMulDivExpr(self, ctx:SvonParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by SvonParser#parenExpr.
    def enterParenExpr(self, ctx:SvonParser.ParenExprContext):
        pass

    # Exit a parse tree produced by SvonParser#parenExpr.
    def exitParenExpr(self, ctx:SvonParser.ParenExprContext):
        pass


    # Enter a parse tree produced by SvonParser#idExpr.
    def enterIdExpr(self, ctx:SvonParser.IdExprContext):
        pass

    # Exit a parse tree produced by SvonParser#idExpr.
    def exitIdExpr(self, ctx:SvonParser.IdExprContext):
        pass



del SvonParser