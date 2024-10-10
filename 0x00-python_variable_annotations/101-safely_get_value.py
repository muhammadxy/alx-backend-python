#!/usr/bin/env python3

"""
This module contains the correct type annotations to the function
from the following parameters and return values:
Hint: Look into TypeVar.
def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
"""

from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any, default: Union[T, None] = None
        ) -> Union[Any, T]:

    """
    Returns the key value from the dictionary if it exists.
    If the key does not exist, returns the default value.
    """

    if key in dct:
        return dct[key]
    else:
        return default
