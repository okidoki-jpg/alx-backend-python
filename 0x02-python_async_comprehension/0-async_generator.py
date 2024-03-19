#!/usr/bin/env python3
"""
Module Doc: Async Generator

Attributes:
    None

Return:
    Asynchronous generator yielding random float numbers between 0 and 10.
"""
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """
    async_generator function:
    loops 1 times to generate random float asynchonously
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
