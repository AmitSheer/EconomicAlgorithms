import itertools

import numpy as np
from numpy import ndarray
from sympy.utilities.iterables import multiset_permutations

"""
get a matrix of value
"""
from typing import List, Dict


def get_sum(mat: List[List[int]], order: List[int], skip: int, max: int) -> int:
    return max - mat[skip][order.index(skip)]


# GREEDY
def VCG_greedy(value_mat: List[List]) -> (List[tuple], tuple, List[int]):
    """
    >>> mat =[[10, 3, 5],[7, 8, 2],[11, 10, 7]]
    >>> VCG_greedy(mat)
    ([(6, 10, 4), (5, 8, 3), (0, 7, 7)], (11, 25, 14), (0, 1, 2))


    """
    # get all permutations of array
    all_values_order = np.array([i for i in range(0, len(value_mat))])
    all_permutation_values = []
    all_per = list(itertools.permutations(all_values_order))
    # get all values of permutations
    for per in all_per:
        all_permutation_values.append(np.sum([value_mat[i][per.index(i)] for i in per]))

    # index of max value
    index_of_choice = np.argmax(all_permutation_values)

    # changes after the calculations of without a certain player
    all_variations_of_calculations: List[tuple] = []

    # get all permutations without one value of player
    # and get the changes values
    for i in range(len(value_mat)):
        max_sum = [get_sum(value_mat, per, i, all_permutation_values[all_per.index(per)]) for per in all_per]
        index = np.argmax(max_sum)

        if index != index_of_choice:
            all_variations_of_calculations.append(
                tuple([
                    # payment,
                    all_permutation_values[index_of_choice] - max_sum[index],
                    # value,
                    value_mat[i][all_per[index_of_choice].index(i)],
                    #
                    abs(value_mat[i][all_per[index_of_choice].index(i)] - (
                                all_permutation_values[index_of_choice] - max_sum[index]))
                ]
                )
            )
        else:
            all_variations_of_calculations.append(
                tuple([
                    # payment,
                    0,
                    # value,
                    value_mat[i][all_per[index_of_choice].index(i)],
                    #
                    value_mat[i][all_per[index_of_choice].index(i)]
                ]
                )
            )
    return all_variations_of_calculations, tuple([
        np.sum([j[0] for j in all_variations_of_calculations]),
        np.sum([j[1] for j in all_variations_of_calculations]),
        np.sum([j[2] for j in all_variations_of_calculations]),
    ]), all_per[index_of_choice]



if __name__ == '__main__':
    l = [
        [10, 3, 5],
        [7, 8, 2],
        [11, 10, 7],
    ]
    print(VCG_greedy(l))
    # #
    # import doctest
    #
    # doctest.testmod()
