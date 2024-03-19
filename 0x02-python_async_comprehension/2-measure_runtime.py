#!/usr/bin/env python3
"""
Module Doc: Measure Runtime

Attributes:
    None

Return:
    Total runtime of four async_comprehension calls as float.
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime function:
    Measures total runtime of four async_comprehension calls
    using asyncio.gather.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
