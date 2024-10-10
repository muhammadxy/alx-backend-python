#!/usr/bin/env python3

"""
This module contains a type-annotated function make_multiplier() that takes a
float multiplier as an argument and returns a function that multiplies a float
by the multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function takes a float multiplier as an argument and returns
    a function that multiplies a float by the multiplier.
    Returns a function that multiplies a float by the multiplier.
    """
    return (lambda x: x * multiplier)
