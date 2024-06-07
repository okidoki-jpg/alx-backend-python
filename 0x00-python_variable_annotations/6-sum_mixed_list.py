#!/usr/bin/env python3
"""
Module Doc: Complex types - mixed list
Sum up a list of int and float numbers.

Attributes:
    mxd_lst (list<Union<int, float>>): input value

Return:
    sum of list as float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sum_mixed_list function
    """
    return float(sum(mxd_lst))
