import time
from functools import wraps

def timed(fn: object):
    """
    The timed decorator uses the @wraps decorator from the functools module to preserve the original function's name and docstring.
    It defines an inner function that measures the execution time of the decorated function by calculating the difference between the start and end times using time.perf_counter().
    """
    @wraps(fn)
    def inner(*args, **kwargs):
        start = time.perf_counter()

        result = fn(*args, **kwargs)

        end = time.perf_counter()

        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = ["{0} = {1}".format(k,v) for (k,v) in kwargs.items()]

        all_args = args_ + kwargs_

        args_str = ",".join(all_args)

        print("{0}({1}) took {2:.6f}s to run".format(fn.__name__,
                                                   args_str,
                                                   elapsed))

        return result

    return inner


@timed
def calc_fibonachi(n):
    """
    This function calculates the nth Fibonacci number using dynamic programming.

    Args:
        n: The index of the Fibonacci number to calculate.

    Returns:
        The nth Fibonacci number.
    """

    cache = {}
    for i in range(n + 1):
        cache[i] = i if i <= 1 else cache[i-1] + cache[i-2]
    return cache[n]

print(calc_fibonachi(55))