#!/usr/bin/env python3
""" From the previous file, import wait_n into 2-measure_runtime """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ From previous file, import wait_n into 2-measure_runtime """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
