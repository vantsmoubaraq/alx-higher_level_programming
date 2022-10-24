#!usr/bin/python3
"""This is a class that inherits from list and print outs a a sorted list"""


class MyList(list):
    """Thi is a class that inherits from list and print outs a a sorted list"""

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
