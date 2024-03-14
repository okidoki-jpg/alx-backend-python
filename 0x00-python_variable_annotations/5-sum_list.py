#!/usr/bin/env python3
"""
Module Doc: Complex types - list of floats
Sum up floats from a list

Attributes:
    input_list (list<float>): inout value

Return:
    sum of list as float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    sum_list function
    """
    return float(sum(input_list))
