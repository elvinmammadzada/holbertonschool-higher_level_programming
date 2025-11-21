#!/usr/bin/python3
from hidden_4 import *

if __name__ == "__main__":
    for name in sorted(dir()):
        if not name.startswith("__"):
            print(name)
