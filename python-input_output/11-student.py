#!/usr/bin/python3
"""Student module with JSON serialization and reloading"""

class Student:
    """Defines a student with first_name, last_name, and age"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation of the student.
        If attrs is a list of strings, only include those attributes.
        """
        student_dict = self.__dict__.copy()
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: v for k, v in student_dict.items() if k in attrs}
        return student_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the student instance from a dictionary"""
        if isinstance(json, dict):
            for key, value in json.items():
                setattr(self, key, value)
