#!/usr/bin/python3
"""module"""


def is_same_class(obj, a_class):
    """Function that returns True if the object is
       exactly an instance of the specified class
        """
    return type(obj) is a_class
