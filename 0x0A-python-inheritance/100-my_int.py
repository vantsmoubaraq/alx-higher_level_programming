#!usr/bin/python3

""" class MyInt that inherits from int"""

class MyInt(Int):
    """Implement a rebel int class"""
    def __new__(cls, *args, *kwargs):
        return (super(MyInt, cls).__new__(cls, *args, *kwargs))

    de __eq__(self, other):
        return int(self) != other

    def __ne__(self , other):
        return int(self) != other

