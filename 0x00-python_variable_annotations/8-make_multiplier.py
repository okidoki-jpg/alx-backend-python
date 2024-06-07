#!/usr/bin/env python3
"""
Module Doc: Complex types - functions
Annoted multiplication of input by a multiplier

Attributes:
    multiplier (float): multiolier input value.

Return:
    input multiplied by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier function.
    """
    return lambda x: x * multiplier
