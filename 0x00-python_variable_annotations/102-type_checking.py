#!/usr/bin/env python3
"""
Module Doc: Type Checking
Create multiple copies of items in a tuple.

Attributes:
    lst (Tuple): input tuple
    factor (int, optional): zoom factor (default is 2)

Return:
    zoomed-in list with copies of items from the input tuple
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    zoom_array function
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
