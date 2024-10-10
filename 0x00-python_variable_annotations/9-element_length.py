#!/usr/bin/env python3

"""
This module contains a type-annotated function that takes
parameters and returns a list of values.
"""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This function takes a list of parameters
    and returns a list of values.
    """
    return [(i, len(i)) for i in lst]
