#!/usr/bin/python3
"""Student class module"""


class Student:
    """Defines a student with first_name, last_name, age"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation; filter attributes if attrs is a list"""
        if isinstance(attrs, list):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__.copy()
