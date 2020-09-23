from functools import wraps
from time import perf_counter
import math

#Creating a measurement decorator
def measure_exe(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        temp = func(*args, **kwargs)
        end = perf_counter()
        runtime = end - start
        print(f"Time: {runtime}")
        return temp
    return wrapper

#Example with custom test factorial function
@measure_exe
def test_timer(x):
    test = sum([math.factorial(x)**2 for j in range(x)])
    return str(test)[:8] #Can be a very big int

test_timer(3000)