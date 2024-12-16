from antlr4 import *
from util.SvonLexer import SvonLexer
from util.SvonParser import SvonParser
import svoner
import sys


def main():
    try:
        visitor = visitors.Svoner()

        if len(sys.argv) > 1:
            with open(sys.argv[1], 'r') as file:
                input_text = file.read()

            input_stream = InputStream(input_text)
            lexer = SvonLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = SvonParser(stream)

            try:
                tree = parser.program()
                visitor.visit(tree)
            except Exception as e:
                print(f"Error: {e}")

        else:
            print("Привет, это наша лабораторная работа, введи текст для компилятора (команда 'exit', чтоб выйти):")

            while True:
                input_text = input("> ")

                if input_text.strip().lower() == "exit":
                    print("Выходим из компилятора.")
                    break

                input_stream = InputStream(input_text)
                lexer = SvonLexer(input_stream)
                stream = CommonTokenStream(lexer)
                parser = SvonParser(stream)

                try:
                    tree = parser.program()
                    visitor.visit(tree)
                except Exception as e:
                    print(f"Error: {e}")

    except Exception:
        print("Компилятор завершил свою работу принудительно.")


if __name__ == '__main__':
    main()