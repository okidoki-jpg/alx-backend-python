#!/usr/bin/env python3
"""
Module Doc: More involved type annotations

Attributes:
    dct (Mapping): input dictionary
    key (Any): input key
    default (Union[T, None], optional): default  (None)

Return:
    value associated with the key if found, else default value
"""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    safely_get_value function
    """
    if key in dct:
        return dct[key]
    else:
        return default
