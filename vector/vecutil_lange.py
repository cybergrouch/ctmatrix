# Copyright 2013 Philip N. Klein
from vec import Vec

def list2vec(L):
    """Given a list L of field elements, return a Vec with domain {0...len(L)-1}
    whose entry i is L[i]

    >>> list2vec([10, 20, 30])
    Vec({0, 1, 2},{0: 10, 1: 20, 2: 30})
    """
    return Vec(set(range(len(L))), {k:L[k] for k in range(len(L))})

def zero_vec(D):
    """Returns a zero vector with the given domain
    """
    return Vec(D, {})
    
def triangular_solve_n(coefficient_vector_list, constant_list):
    D = coefficient_vector_list[0].D
    n = len(D)
    assert D == set(range(n))
    x = zero_vec(D)
    for i in reversed(range(n)):
        x[i] = (constant_list[i] - coefficient_vector_list[i] * x) / coefficient_vector_list[i][i]
    return x

def triangular_solve(coefficient_vector_list, label_list, constant_list):
    D = coefficient_vector_list[0].D
    n = len(D)
    assert D == set(label_list)
    x = zero_vec(D)
    for i,k in reversed(list(enumerate(label_list))):
        x[k] = (constant_list[i] - coefficient_vector_list[i] * x) / coefficient_vector_list[i][k]
    return x

