#!/usr/bin/env python3
""" measures the total exection time """

import asyncio
import time
import random
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int = 0, max_delay: int = 10) -> float:
    """ 
    agrs:
    n and max_delays

    Returns Total_time/n
    """
    first_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - first_time
    total_time = elapsed / n     

    return total_time                                                                                                                                                                                                                                                                                                                                                  
