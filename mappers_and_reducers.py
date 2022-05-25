import numpy as np


def bigram_emitter(inputs):
    """
    Emits the input with count 1 as a tuple
    """
    return inputs, 1


def bigram_reducer(inputs):
    """
    Reducer function for the bigram problem.
    """
    return inputs[0], sum(inputs[1])


def no_map(inputs):
    return inputs


def reduce_to_matrix(bigram_dict):
    matrix = np.zeros((28, 28))
    indexlst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', '#', '_']
    matrix[indexlst.index(bigram_dict[0][0]), indexlst.index(bigram_dict[0][1])] = bigram_dict[1][0]
    return matrix
