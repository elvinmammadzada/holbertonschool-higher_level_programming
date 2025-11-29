#!/usr/bin/python3
"""1-write_file module"""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file.
    Return the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
