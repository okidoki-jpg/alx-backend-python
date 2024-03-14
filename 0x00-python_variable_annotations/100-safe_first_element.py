#!/usr/bin/env python3
"""
Module Doc: Duck typing - first element of a sequence
Retrieves the first element of a sequence if it exists.

Attributes:
    lst (Sequence[Any]): input sequence

Return:
    first element of sequence if it exists, otherwise None
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    safe_first_element function
    """
    if lst:
        return lst[0]
    else:
        return None
