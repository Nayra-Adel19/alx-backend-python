#!/usr/bin/env python3
""" Write asynchronous coroutine that takes in integer argument """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Write asynchronous coroutine that takes in integer argument """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
