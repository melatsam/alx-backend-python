#!/usr/bin/env python3
""" coroutine that takes random delay"""

import asyncio
import random 

async def wait_random(max_delay: int = 10) -> float:
    """ 
    max_delay - await time

    Return the delay time
    """
delay: float = random.uniform(0, max_delay)
await asyncio.sleep(delay)

return delay
