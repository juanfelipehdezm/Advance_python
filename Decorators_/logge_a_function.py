from functools import wraps
from datetime import datetime, timezone
import time

def logged(fn):
    """
    This code defines a decorator called logged that can be used to log the function call and execution time of any function it is applied to.
    """
    @wraps(fn)
    def inner(*args, **kwargs):
        """
        Decorator that logs the function call and its execution time.
        Args:
            fn: The function to be logged.
        Returns:
            The wrapped function.
        """
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print('{0}: called at {1}'.format(fn.__name__, run_dt))
        return result
        
    return inner


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

#This is also known as STACKED DECORATORS
@timed
@logged
def factorial(n):
    from operator import mul
    from functools import reduce
    
    return reduce(mul, range(1, n+1))


print(factorial(10))