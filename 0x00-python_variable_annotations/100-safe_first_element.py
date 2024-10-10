#!/usr/bin/env python3

"""
This module contains the Augment Code with the correct duck-typed annotations
from the following code:
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Duck-typed version of the safe_first_element function.
    """
    if lst:
        return lst[0]
    else:
        return None
