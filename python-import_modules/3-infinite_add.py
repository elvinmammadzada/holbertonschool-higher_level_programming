#!/usr/bin/python3
from sys import argv


def main():
    total = sum(map(int, argv[1:]))
    print(total)


if __name__ == "__main__":
    main()
