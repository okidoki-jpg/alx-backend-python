#!/usr/bin/env python3
"""
Module Doc: Complex types - string and int/float to tuple
Return tupple with k as str and v squared

Attributes:
    k (str): input value
    v (int, float): input value

Return:
    A tupple with k as str and v squared
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    to_kv function
    """
    return (k, float(v**2))
