# Miny Compiler

A simple compiler for the COMPY language, implemented in Python.
It performs **lexical analysis**, **parsing**, and generates a **syntax tree**. The syntax tree will be visualized as a diagram using Graphviz.

---

## Features

* Tokenizes source code according to COMPY language specification.
* Parses simple assignment and arithmetic statements (`id = expr;`).
* Detects **lexical** and **syntax errors** with informative messages.
* Generates **text-based abstract syntax trees (AST)**.
* Optionally visualizes AST as a **PNG diagram**.

---

## Requirements

* Python 3.10+
* [Graphviz](https://graphviz.org/download/) installed and added to your system PATH (the `bin` folder, e.g., `C:\Program Files\Graphviz\bin`).
* Python packages:

  ```bash
  pip install graphviz
  ```

---

## Folder Structure

```
cpt316-asg1/
├── compiler/               # Core compiler modules
│   ├── __init__.py
│   ├── lexer.py            # Lexical analyzer
│   ├── parser.py           # Parser for syntax analysis
│   ├── ast.py              # AST utilities (e.g., print_tree)
│   └── graph.py            # AST visualization using Graphviz
├── main.py                 # Entry point; reads source code and calls compiler functions
└── README.md               # Project documentation
```

---

## Usage

1. Open a terminal (or PyCharm terminal) in the project root.
2. Run the compiler:

   ```bash
   python main.py
   ```
3. Enter COMPY source code when prompted, for example:

   ```
   Enter source code: x = y + 3;
   ```
4. To quit the compiler, type:

   ```
   quit
   ```
5. A PNG file `syntax_tree.png` will popped out and stored in the project folder.

---

## Team Members

1. Lim Wei Ling (22306277)
2. Ng Xuan Hern (22304061)
3. Harini Subramaniam (22303876)
4. Nadiah Shahirah binti Mohamad Zaki (22300068)
