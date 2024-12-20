import time

from util.SvonParser import SvonParser
from util.SvonVisitor import SvonVisitor

variables = {}  # Хранит значения переменных
labels, t_var_num = 1, 1  # Счетчики для меток и временных переменных
lines = []  # Список строк для хранения промежуточного кода

# Обрабатывает аргументы, которые могут быть либо числом, либо кортежем
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

# Создаёт уникальное имя временной переменной (например, t1, t2).
def get_var_num():
    global t_var_num
    t_var_num += 1
    return f"t{t_var_num - 1}"

# Генерирует уникальную метку (например, L1, L2)
def get_label():
    global labels
    labels += 1
    return f"L{labels - 1}"

# Записывает строки промежуточного кода в файл file.txt
def fill_file():
    with open('file.txt', 'w') as f:
        for line in lines:
            f.write(line)



class Svoner(SvonVisitor):

    # обход программы
    def visitProgram(self, ctx: SvonParser.ProgramContext):
        self.visitChildren(ctx)
        fill_file()
        return

    def visitStatement(self, ctx: SvonParser.StatementContext):
        return self.visitChildren(ctx)

    # Выполняет команду print и добавляет её в промежуточный код
    def visitPrintStatement(self, ctx: SvonParser.PrintStatementContext):
        value = self.visit(ctx.expression())
        if isinstance(value, tuple):
            value_val, value_tmp = value[0], value[1]
        else:
            value_val, value_tmp = value, value
        lines.append(f"print {value_val}\n")
        print(value_val)

    # Обрабатывает присваивание переменной
    def visitAssignmentStatement(self, ctx: SvonParser.AssignmentStatementContext):
        var_name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())

        if isinstance(value, tuple):
            value_val, value_tmp = value[0], value[1]
        else:
            value_val, value_tmp = value, value

        variables[var_name] = value_val
        lines.append(f"{var_name} = {value_tmp}\n")

    # Генерирует промежуточный код для условного оператора if
    def visitIfStatement(self, ctx: SvonParser.IfStatementContext):
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

    def visitNumberExpr(self, ctx: SvonParser.NumberExprContext):
        return int(ctx.NUMBER().getText())

    def visitStringExpr(self, ctx: SvonParser.StringExprContext):
        return ctx.STRING().getText()[1:-1]

    def visitIdExpr(self, ctx: SvonParser.IdExprContext):

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

    #Генерирует код для операций сложения и вычитания.
    def visitAddSubExpr(self, ctx: SvonParser.AddSubExprContext):
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

            if ctx.op.type == SvonParser.PLUS:
                lines.append(f"{t} = {left_tmp} + {right_tmp}\n")
                return str(left_val) + str(right_val)
            elif ctx.op.type == SvonParser.MINUS:
                raise ValueError("Cannot subtract strings.\n")

        # Сложение чисел
        else:

            vals = get_args(left, right)
            left_val, left_tmp, right_val, right_tmp = vals[0], vals[1], vals[2], vals[3]

            if ctx.op.type == SvonParser.PLUS:
                lines.append(f"{t} = {left_tmp} + {right_tmp}\n")
                return left_val + right_val, t
            else:
                lines.append(f"{t} = {left_tmp} - {right_tmp}\n")
                return left_val - right_val, t

    # Операции умножения и деления
    def visitMulDivExpr(self, ctx: SvonParser.MulDivExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        t = get_var_num()

        vals = get_args(left, right)
        left_val, left_tmp, right_val, right_tmp = vals[0], vals[1], vals[2], vals[3]

        op_map = {
            SvonParser.MUL: left_val * right_val,
            SvonParser.DIV: left_val // right_val,
            SvonParser.POW: pow(left_val, right_val),
            SvonParser.MOD: left_val % right_val
        }

        if ctx.op.type in op_map:
            operator = SvonParser.literalNames[ctx.op.type].strip("\'")
            lines.append(f"{t} = {left_tmp} {operator} {right_tmp}\n")
            return op_map[ctx.op.type], t
        else:
            raise ValueError(f"Unknown comparison operator: {ctx.op.type}\n")

    def visitComparisonExpr(self, ctx: SvonParser.ComparisonExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        t = get_var_num()

        vals = get_args(left, right)
        left_val, left_tmp, right_val, right_tmp = vals[0], vals[1], vals[2], vals[3]

        op_map = {
            SvonParser.GT: left_val > right_val,
            SvonParser.LT: left_val < right_val,
            SvonParser.GE: left_val >= right_val,
            SvonParser.LE: left_val <= right_val,
            SvonParser.EQ: left_val == right_val,
            SvonParser.NEQ: left_val != right_val
        }

        if ctx.op.type in op_map:
            operator = SvonParser.literalNames[ctx.op.type].strip("\'")
            lines.append(f"{t} = {left_tmp} {operator} {right_tmp}\n")
            return op_map[ctx.op.type], t
        else:
            raise ValueError(f"Unknown comparison operator: {ctx.op.type}")

    def visitLogicalExpr(self, ctx: SvonParser.LogicalExprContext):
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


        if ctx.op.type == SvonParser.AND:
            lines.append(f"{t} = {left_tmp} && {right_val}\n")
            return left_val and right_val, t
        else:
            lines.append(f"{t} = {left_tmp} || {right_val}\n")
            return left_val or right_val, t

    def visitNotExpr(self, ctx: SvonParser.NotExprContext):
        value = self.visit(ctx.expression())
        t = get_var_num()
        if isinstance(value, tuple):
            value_val, value_tmp = bool(value[0]), str(value[1])
        else:
            value_val, value_tmp = bool(value), bool(value)
        lines.append(f"{t} = !{value_tmp}\n")
        return not value_val

    def visitParenExpr(self, ctx: SvonParser.ParenExprContext):
        return self.visit(ctx.expression())

    def visitForStatement(self, ctx: SvonParser.ForStatementContext):
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

    def visitWhileStatement(self, ctx: SvonParser.WhileStatementContext):
        label_start = get_label()
        label_end = get_label()
        lines.append(f"ifFalse {self.visit(ctx.expression())[1]} goto {label_end}\n")
        lines.append(f"{label_start}:\n")
        while self.visit(ctx.expression())[0]:
            for statement in ctx.statement():
                self.visit(statement)
        lines.append(f"goto {label_start}\n")
        lines.append(f"{label_end}:\n")