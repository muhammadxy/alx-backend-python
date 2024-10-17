#!/usr/bin/env python3

"""
This module import `async_generator` function from previous module
and then contains a coroutine called `async_comprehension` that takes
no arguments.
The coroutine will collect 10 random numbers using an async comprehensing over
`async_generator`, then return the 10 random numbers.
"""

from typing import List
# Import asyncio module
import asyncio
# Import async_generator function from previous module
async_generator = __import__('0-async_generator').async_generator


# Define async_comprehension function with no arguments
async def async_comprehension() -> List[float]:
    """
    This coroutine will collect 10 random numbers using an async comprehensing
    over `async_generator`, then return the 10 random numbers.
    """
    return [number async for number in async_generator()]
