#!/usr/bin/env python3

"""
This module contains a type-annotated function to_kv() that takes a string `k`
and an int OR float v as arguments and returns a tuple.
The first element of the tuple is the string `k` and the second element is the
square of the int OR float `v` and should be annotated as a float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function takes a string `k` and an int OR float v as arguments and
    returns a tuple.
    Returns a tuple of the form (string, float)
    """
    return (k, v * v)
