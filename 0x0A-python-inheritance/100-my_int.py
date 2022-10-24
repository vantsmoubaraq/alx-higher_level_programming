#!/usr/bin/python3
""" MyInt module"""


class MyInt(int):
    """ class MyInt that inherits from int"""

    def __ne__(self, next):
        """ negation to equal """
        return super().__eq__(next)

    def __eq__(self, next):
        """ equal to negation """
        return super().__ne__(next)
