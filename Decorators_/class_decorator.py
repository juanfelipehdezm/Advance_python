from time import perf_counter

class timed:
    """
        A decorator class that measures the average run time of a function over multiple repetitions.

    Args:
        reps: The number of times the function should be executed.

    Returns:
        The result of the decorated function.

    Examples:
        @timed(reps=5)
        def my_function():
            pass
    """
    def __init__(self, reps):
        self.reps = reps

    def __call__(self,fn):
        def inner(*args, **kwargs):
            total_elapse = 0
            for i in range(self.reps):
                start = perf_counter()
                #executing the function
                result = fn(*args, *kwargs)
                end = perf_counter()

                total_elapse += (end - start)
            
            avg_run_time = total_elapse / self.reps
            print("Avg Run Time: {0:.6f}s for {1} reps".format(avg_run_time,
                                                                self.reps))
            
            return result
        return inner
    

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