#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:

    """Base Geometry class empty"""

    def area(self):
        """Area function"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integer value
        Args:
            name (str): string name
            value (int): value to be validated
        Raises:
            TypeError: if not an integer
            ValueError: if less or equal to 0
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
