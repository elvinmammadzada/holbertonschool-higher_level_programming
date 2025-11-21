#!/usr/bin/python3
from sys import argv

def main():
    total = sum(list(map(int, argv[1:])))
    print(total)

