#!usr/bin/python3
"""This is a class that inherits from list and print outs a a sorted list"""


class MyList(list):
    """Thi is a class that inherits from list and print outs a a sorted list"""

    def print_sorted(self):
        print(sorted(self))
