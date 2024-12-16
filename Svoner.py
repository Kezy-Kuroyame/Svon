import time

from util.OurLangParser import OurLangParser
from util.OurLangVisitor import OurLangVisitor

variables = {}
labels, t_var_num = 1, 1
lines = []


def get_args(left, right):
    if isinstance(left, tuple):
        left_val, left_tmp = int(left[0]), str(left[1])
    else:
        left_val, left_tmp = int(left), int(left)

    if isinstance(right, tuple):
        right_val, right_tmp = int(right[0]), str(right[1])
    else:
        right_val, right_tmp = int(right), int(right)
    return left_val, left_tmp, right_val, right_tmp


def get_var_num():
    global t_var_num
    t_var_num += 1
    return f"t{t_var_num - 1}"


def get_label():
    global labels
    labels += 1
    return f"L{labels - 1}"


def fill_file():
    with open('file.txt', 'w') as f:
        for line in lines:
            f.write(line)



class OurVisitor(OurLangVisitor):

    def visitProgram(self, ctx: OurLangParser.ProgramContext):
        self.visitChildren(ctx)
        fill_file()
        return

    def visitStatement(self, ctx: OurLangParser.StatementContext):
        return self.visitChildren(ctx)

    def visitPrintStatement(self, ctx: OurLangParser.PrintStatementContext):
        value = self.visit(ctx.expression())
        if isinstance(value, tuple):
            value_val, value_tmp = value[0], value[1]
        else:
            value_val, value_tmp = value, value
        lines.append(f"print {value_val}\n")
        print(value_val)

    def visitAssignmentStatement(self, ctx: OurLangParser.AssignmentStatementContext):
        var_name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())

        if isinstance(value, tuple):
            value_val, value_tmp = value[0], value[1]
        else:
            value_val, value_tmp = value, value

        variables[var_name] = value_val
        lines.append(f"{var_name} = {value_tmp}\n")

    def visitIfStatement(self, ctx: OurLangParser.IfStatementContext):
        condition = self.visit(ctx.expression())
        if isinstance(condition, tuple):
            condition_val, condition_tmp = bool(condition[0]), str(condition[1])
        else:
            condition_val, condition_tmp = bool(condition), str(condition)

        label_start = get_label()
        lines.append(f"ifFalse {condition_tmp} goto {label_start}\n")

        label_end = get_label()
        lines.append(f"goto {label_end}\n")

        lines.append(f"{label_start}:\n")
        if condition_val:
            for statement in ctx.statement():
                self.visit(statement)
            lines.append(f"goto {label_end}\n")
            return


        if ctx.elifStatement():
            for elif_statement in ctx.elifStatement():
                elif_condition = self.visit(elif_statement.expression())

                if isinstance(elif_condition, tuple):
                    elif_condition_val, elif_condition_tmp = bool(elif_condition[0]), str(elif_condition[1])
                else:
                    elif_condition_val, elif_condition_tmp = bool(elif_condition), str(elif_condition)
                elif_label = get_label()
                lines.append(f"ifFalse {elif_condition_tmp} goto {elif_label}\n")
                lines.append(f"{elif_label}:\n")
                if elif_condition_val:
                    for statement in elif_statement.statement():
                        self.visit(statement)
                    lines.append(f"goto {label_end}\n")
                    return

        if ctx.elseStatement():
            for statement in ctx.elseStatement().statement():
                self.visit(statement)
            lines.append(f"goto {label_end}\n")
            return

        lines.append(f"{label_end}:\n")

    def visitNumberExpr(self, ctx: OurLangParser.NumberExprContext):
        return int(ctx.NUMBER().getText())

    def visitStringExpr(self, ctx: OurLangParser.StringExprContext):
        return ctx.STRING().getText()[1:-1]

    def visitIdExpr(self, ctx: OurLangParser.IdExprContext):

        var_name = ctx.IDENTIFIER().getText()

        # Обработка булевых значений
        if var_name == "true":
            return True
        elif var_name == "false":
            return False

        value = variables.get(var_name, None)
        if value is None:
            print(f"Warning: Variable '{var_name}' is not defined.\n")
            return 0
        return value

    def visitAddSubExpr(self, ctx: OurLangParser.AddSubExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        t = get_var_num()

        # Сложение строк
        if isinstance(left, str) or isinstance(right, str):

            if isinstance(left, tuple):
                left_val, left_tmp = str(left[0]), str(left[1])
            else:
                left_val, left_tmp = str(left), str(left)

            if isinstance(right, tuple):
                right_val, right_tmp = str(right[0]), str(right[1])
            else:
                right_val, right_tmp = str(right), str(right)

            if ctx.op.type == OurLangParser.PLUS:
                lines.append(f"{t} = {left_tmp} + {right_tmp}\n")
                return str(left_val) + str(right_val)
            elif ctx.op.type == OurLangParser.MINUS:
                raise ValueError("Cannot subtract strings.\n")

        # Сложение чисел
        else:

            vals = get_args(left, right)
            left_val, left_tmp, right_val, right_tmp = vals[0], vals[1], vals[2], vals[3]

            if ctx.op.type == OurLangParser.PLUS:
                lines.append(f"{t} = {left_tmp} + {right_tmp}\n")
                return left_val + right_val, t
            else:
                lines.append(f"{t} = {left_tmp} - {right_tmp}\n")
                return left_val - right_val, t

    def visitMulDivExpr(self, ctx: OurLangParser.MulDivExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        t = get_var_num()

        vals = get_args(left, right)
        left_val, left_tmp, right_val, right_tmp = vals[0], vals[1], vals[2], vals[3]

        op_map = {
            OurLangParser.MUL: left_val * right_val,
            OurLangParser.DIV: left_val // right_val,
            OurLangParser.POW: pow(left_val, right_val),
            OurLangParser.MOD: left_val % right_val
        }

        if ctx.op.type in op_map:
            operator = OurLangParser.literalNames[ctx.op.type].strip("\'")
            lines.append(f"{t} = {left_tmp} {operator} {right_tmp}\n")
            return op_map[ctx.op.type], t
        else:
            raise ValueError(f"Unknown comparison operator: {ctx.op.type}\n")

    def visitComparisonExpr(self, ctx: OurLangParser.ComparisonExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        t = get_var_num()

        vals = get_args(left, right)
        left_val, left_tmp, right_val, right_tmp = vals[0], vals[1], vals[2], vals[3]

        op_map = {
            OurLangParser.GT: left_val > right_val,
            OurLangParser.LT: left_val < right_val,
            OurLangParser.GE: left_val >= right_val,
            OurLangParser.LE: left_val <= right_val,
            OurLangParser.EQ: left_val == right_val,
            OurLangParser.NEQ: left_val != right_val
        }

        if ctx.op.type in op_map:
            operator = OurLangParser.literalNames[ctx.op.type].strip("\'")
            lines.append(f"{t} = {left_tmp} {operator} {right_tmp}\n")
            return op_map[ctx.op.type], t
        else:
            raise ValueError(f"Unknown comparison operator: {ctx.op.type}")

    def visitLogicalExpr(self, ctx: OurLangParser.LogicalExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        t = get_var_num()

        if isinstance(left, tuple):
            left_val, left_tmp = bool(left[0]), str(left[1])
        else:
            left_val, left_tmp = bool(left), bool(left)

        if isinstance(right, tuple):
            right_val, right_tmp = bool(right[0]), str(right[1])
        else:
            right_val, right_tmp = bool(right), bool(right)


        if ctx.op.type == OurLangParser.AND:
            lines.append(f"{t} = {left_tmp} && {right_val}\n")
            return left_val and right_val, t
        else:
            lines.append(f"{t} = {left_tmp} || {right_val}\n")
            return left_val or right_val, t

    def visitNotExpr(self, ctx: OurLangParser.NotExprContext):
        value = self.visit(ctx.expression())
        t = get_var_num()
        if isinstance(value, tuple):
            value_val, value_tmp = bool(value[0]), str(value[1])
        else:
            value_val, value_tmp = bool(value), bool(value)
        lines.append(f"{t} = !{value_tmp}\n")
        return not value_val

    def visitParenExpr(self, ctx: OurLangParser.ParenExprContext):
        return self.visit(ctx.expression())

    def visitForStatement(self, ctx: OurLangParser.ForStatementContext):
        self.visit(ctx.declaration)
        label_start = get_label()
        label_end = get_label()
        lines.append(f"{label_start}:\n")
        lines.append(f"ifFalse {self.visit(ctx.expression())[1]} goto {label_end}\n")
        while self.visit(ctx.expression())[0]:
            for statement in ctx.statement():
                self.visit(statement)
            self.visit(ctx.assignment)
        lines.append(f"goto {label_start}\n")
        lines.append(f"{label_end}:\n")

    def visitWhileStatement(self, ctx: OurLangParser.WhileStatementContext):
        label_start = get_label()
        label_end = get_label()
        lines.append(f"ifFalse {self.visit(ctx.expression())[1]} goto {label_end}\n")
        lines.append(f"{label_start}:\n")
        while self.visit(ctx.expression())[0]:
            for statement in ctx.statement():
                self.visit(statement)
        lines.append(f"goto {label_start}\n")
        lines.append(f"{label_end}:\n")