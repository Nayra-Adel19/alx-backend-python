#!/usr/bin/env python3
""" Import async_comprehension from the previous file and write """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Import async_comprehension from the previous file and write """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
