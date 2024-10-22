# import os
# import sys


def greet(name):
    print(f"Hello, {name}!")  # Intentionally correct formatted line


def add(a, b):  # Missing space after comma
    return a + b  # Wrong indentation (Black should fix this)


greet("World")  # Extra space inside parentheses (Black should fix this)

# Trailing whitespace issue below (this should be removed by pre-commit)
greet("Pre-commit")
