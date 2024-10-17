#!/usr/bin/env python3

"""
This module import `async_comprehension` function from previous module
and then contains a coroutine called `measure_runtime` that will execute
the `async_comprehension` coroutine four times in parallel using the
`asyncio.gather` function.
The measure_runtime should measure the total runtime and return it.
"""

# import asyncio and time modules
import asyncio
import time
# import async_comprehension function from previous module
async_comprehension = __import__('1-async_comprehension').async_comprehension


# define measure_runtime function with no arguments
async def measure_runtime() -> float:
    """
    This coroutine will measure the total runtime of the `async_comprehension`
    coroutine four times in parallel using the `asyncio.gather` function.
    """
    start = time.perf_counter()  # start timer
    # execute async_comprehension four times in parallel using asyncio.gather
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    # stop timer and calculate total runtime
    total = time.perf_counter() - start
    return total
