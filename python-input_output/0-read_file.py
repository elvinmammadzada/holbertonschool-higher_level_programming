#!/usr/bin/python3
"""Python read file content"""


def read_file(filename=""):
    """readfile function for reading"""
    with open(filename, "r") as f:
        print(f.read(), end="")
