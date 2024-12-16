# Основы разработки компиляторов - SVON

## Docker
build: docker build -t a:latest .

run: docker run --rm -v ${PWD}:/dir -it a

## В запущенном Докере
build: antlr4 -Dlanguage=Python3 -o util -visitor Svon.g4

run: python3 main.py

