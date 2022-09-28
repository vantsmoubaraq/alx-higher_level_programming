#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return(list(map(lambda list_a:list(map((lambda elm: elm * elm, list_a)),matrix))))
