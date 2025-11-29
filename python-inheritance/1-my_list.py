#!/usr/bin/python3
"""1-my_list module"""


class MyList(list):
    """Inherits from list and adds a print_sorted method."""

    def print_sorted(self):
        """Print the list in ascending order without modifying the original."""
        print(sorted(self))
