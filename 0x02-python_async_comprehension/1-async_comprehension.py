#!/usr/bin/env python3
""" Import async_generator from the previous task and then write """
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """ Import async_generator from the previous task and then write """
    return [b async for b in async_generator()]
