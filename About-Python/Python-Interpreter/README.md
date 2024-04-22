## Python as an Interpreter

- Python is an interpreted language, which means that it is executed line by line, rather than being compiled into machine code before execution. This allows for a more interactive and flexible development process.

- The Python interpreter is usually installed as `/usr/local/bin/python3.12` on those machines where it is available; putting `/usr/local/bin` in your Unix shell’s search path makes it possible to start it by typing the command:
    - `python3.12`
    - to the shell.1 Since the choice of the directory where the interpreter lives is an installation option, other places are possible; check with your local Python guru or system administrator.

### Storing Long Codes

When working with long codes, it is common to store them in separate files with a `.py` extension. These files can then be imported into other Python scripts using the `import` statement. This helps to organize and modularize your codebase.

### Tools for Python Development

There are several tools commonly used for Python development, including:

- Integrated Development Environments (IDEs) such as PyCharm, Visual Studio Code, and Atom.
- Text editors like Sublime Text and Vim.
- Command-line tools like the Python interpreter itself, which can be used for quick testing and running scripts.

### Python Interpreter Mode

The Python interpreter can be run in interactive mode, allowing you to execute Python code directly and see the results immediately. To start the interpreter, simply type `python` or `python3` in your command prompt or terminal.

In the interpreter mode, you can type Python code directly and press Enter to execute it. This is useful for testing small snippets of code, experimenting with language features, and debugging.

### Connecting to Compiled Python Mode

Python also supports compiled mode, where Python scripts are compiled into bytecode before execution. This bytecode can then be executed by the Python interpreter.

To run a Python script in compiled mode, you can use the `python` command followed by the name of the script file. For example:

