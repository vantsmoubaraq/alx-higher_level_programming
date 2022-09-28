#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    for key, item in a_dictionary.items():
        if value not in a_dictionary.values:
            return a_dictionary
        else:
            if (item == value):
                del a_dictionary[key]
    return a_dictionary
