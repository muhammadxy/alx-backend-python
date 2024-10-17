#!/usr/bin/env python3

"""
This module contains a asynchronous coroutine called `async_generator`
that takes no arguments.The coroutine will loop 10 times, each time
asynchronously wait 1 second, then yield a random number between 0 and 10.
"""

from typing import Generator

# import asyncio and random modules
import asyncio
import random


# Define async_generator function with no arguments
async def async_generator() -> Generator[float, None, None]:
    """
    This coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
    """

    for _ in range(10):  # loop 10 times
        await asyncio.sleep(1)  # async wait 1 second
        yield random.uniform(0, 10)  # yield a random number between 0 and 10
