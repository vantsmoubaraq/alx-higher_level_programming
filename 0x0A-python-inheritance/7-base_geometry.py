#!/usr/bin/python3

"""Creates a class BaseGeometry"""


class BaseGeometry:
    """creates aclass BaseGeometry"""
    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        else:
            if value <= 0:
                raise ValueError("{:s} must be greater than 0".format(name))
