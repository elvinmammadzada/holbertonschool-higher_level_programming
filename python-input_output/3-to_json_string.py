#!/usr/bin/python3
"""3-to_json_string module"""

import json


def to_json_string(my_obj):
    """Return the JSON representation of an object (string)."""
    return json.dumps(my_obj)
