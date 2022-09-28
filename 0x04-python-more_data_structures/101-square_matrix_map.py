#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return(list(map(lambda list_a: map(lambda elm: elm * elm, list_a),matrix)))
