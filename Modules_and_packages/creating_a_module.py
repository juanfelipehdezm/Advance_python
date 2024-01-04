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
