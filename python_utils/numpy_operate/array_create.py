# _*_ coding:utf-8 _*_

"""
This file is about ways to create different types of np.array(),
like identity, diagonal matrix and so on.
"""

import numpy as np


def common_create():
    """
    common way of creating array
    :return: none
    """
    arr1 = np.array([1, 2])
    print arr1
    # [1 2]
    print arr1.shape
    # (2L,)
    arr2 = np.array([[1, 2], [3.1, 4.]])
    print arr2
    # [[ 1.   2. ]
    #  [ 3.1  4. ]]
    print arr2.shape
    # (2L, 2L)
    arr3 = np.array([[1, 2], [3, 4]], dtype=complex)
    print arr3
    # [[ 1.+0.j  2.+0.j]
    #  [ 3.+0.j  4.+0.j]]

if __name__ == '__main__':
    common_create()