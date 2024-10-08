#!/usr/bin/env python3
"""Creating multiple coroutines"""

import bisect
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Wait, execute then returns a list of waiting!"""
    waitings = []
    for i in range(n):
        wait_time = await wait_random(max_delay)
        bisect.insort_left(waitings, wait_time)

    return waitings
