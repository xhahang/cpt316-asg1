import os
os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"

from compiler.lexer import lexer, LexicalError
from compiler.parser import Parser, SyntaxError
from compiler.ast import print_tree
from compiler.graph import build_graph

def compile(code):
    try:
        tokens = lexer(code)    # tokenize input

    except LexicalError as e:
        print("\n" + str(e))
        print("Compilation terminated.\n")
        return None

    # proceed to syntax analysis if lexical analysis is successful
    try:
        parser = Parser(tokens)
        ast = parser.stmt()  # parse one statement
        print("\nSyntax is correct!\n")
        print("Text-based Syntax Tree:")
        print_tree(ast)      # print text-based syntax tree
        print("\n")

        g = build_graph(ast)  # print syntax tree diagram
        g.attr(size="3,3!")
        g.render("syntax_tree", format="png", view=True)
        print("\n\n")

    except SyntaxError as e:
        print("\n" + str(e))
        print("Compilation terminated due to syntax error.\n")
        return None

def main():
  print("=" *45)
  print("Welcome to COMPY Compiler by Group 16 !")
  print("Enter your source code below.")
  print("Or type 'quit' to stop the compiler.")
  print("=" *45)

  while True:
    source_code = input("Enter source code: ")

    if source_code.lower() == "quit":
      print("Goodbye")
      break
    compile(source_code)

if __name__ == "__main__":
  main()