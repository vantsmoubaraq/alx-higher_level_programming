#!/usr/bin/python3
""""Module"""


def add_attribute(obj, name, value):
    """
    adds a new attribute to an object if it’s possible
    Raise a TypeError exception
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
