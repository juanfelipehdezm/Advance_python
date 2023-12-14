from time import perf_counter

#we defined 3 funtions in order to parametize the decorator
def timed(reps: int):
    """
    This code defines a decorator function called timed that can be used 
    to measure the average run time of a function over a specified number of repetitions.
    """
    def decorator(fn):
        def inner(*args, **kwargs):
            total_elapse = 0
            for i in range(reps):
                start = perf_counter()
                #executing the function
                result = fn(*args, *kwargs)
                end = perf_counter()

                total_elapse += (end - start)
            
            avg_run_time = total_elapse / reps
            print("Avg Run Time: {0:.6f}s for {1} reps".format(avg_run_time,
                                                              reps))
            
            return result
        return inner
    return decorator


@timed(10)
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


print(calc_fibonachi(100))