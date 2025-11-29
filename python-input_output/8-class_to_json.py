#!/usr/bin/python3
"""Function that returns the dictionary description for JSON serialization"""

def class_to_json(obj):
    """
    Returns the dictionary representation of an object’s attributes
    for JSON serialization.
    """
    return obj.__dict__.copy()
