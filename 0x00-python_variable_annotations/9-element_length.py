#!/usr/bin/env python3
"""
Module Doc: Let's duck type an iterable object
Enumerate length of values in iterable

Attributes:
    lst (iterable): iterable input value

Return:
    Array with enumerated length of values in iterable
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    element_length function
    """
    return [(i, len(i)) for i in lst]
