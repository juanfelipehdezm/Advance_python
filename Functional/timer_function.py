import time

def time_it(fn: object,rep: int = 1,  *args, **kwargs):
    """
    Average the time it takes a function to run

    Args:
        fn (object): The function to be executed.
        rep (int, optional): The number of times to execute the function. Defaults to 1.
        *args: Variable length argument list to be passed to the function.
        **kwargs: Arbitrary keyword arguments to be passed to the function.

    Returns:
        None

    Examples:
        time_it(my_function, 5, arg1, arg2, kwarg1=value1)
    """
    start = time.perf_counter()
    for _ in range(rep):
        fn(*args, **kwargs)
    
    end = time.perf_counter()

    return round((end - start) / rep,2)


def compute_powers(n, start: int = 1, end = None):
    """
    Computes the powers of a given number.

    Args:
        n: The base number.
        start (int, optional): The starting exponent. Defaults to 1.
        end: The ending exponent. If not provided, it is set to start + 1.

    Returns:
        list: A list of the computed powers of the number.

    Examples:
        compute_powers(2)  # Returns [2]
        compute_powers(2, 1, 4)  # Returns [2, 4, 8, 16]
    """
    if end is None:
        end = start + 1
    return [n**i for i in range(start, end)]

#timing the function
print("In average it took {} segs to run your function.".format(time_it(compute_powers, rep=3, n = 2,start = 0, end = 20000)))
#In average it took 0.26 segs to run your function.