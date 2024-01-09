def fibonacci(n):
    """Calculate the nth value in the Fibonacci sequence.

    Args:
        n (int): The position of the value in the Fibonacci sequence to calculate.
                 Must be a positive integer.

    Returns:
        int or None: The value at the nth position in the Fibonacci sequence.
                     Returns None for invalid input (n <= 0).

    Notes:
        The Fibonacci sequence is a series of numbers where each number is the sum
        of the two preceding ones, starting from 0 and 1.
        The sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, ...

    Examples:
        >>> fibonacci(5)
        3
        >>> fibonacci(10)
        34
        >>> fibonacci(-3)
        None
    """
    
    if n <= 0:
        return None
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)



def lucas(n):
    """Calculate the nth value in the Lucas number sequence.

    Args:
        n (int): The position of the value in the Lucas number sequence to calculate.
                 Must be a non-negative integer.

    Returns:
        int: The value at the nth position in the Lucas number sequence.

    Notes:
        The Lucas sequence is similar to the Fibonacci sequence, where each number
        is the sum of the two preceding ones, but the sequence starts with 2 and 1
        instead of 0 and 1.

    Examples:
        >>> lucas(5)
        11
        >>> lucas(10)
        123
        >>> lucas(0)
        2
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)

def sum_series(n, first=0, second=1):
    """
    Generate a series based on the provided parameters.

    :param n: Determines which element in the series to print.
    :param first: Optional parameter to set the first value in the series (default is 0 for Fibonacci sequence).
    :param second: Optional parameter to set the second value in the series (default is 1 for Fibonacci sequence).
    :return: The nth value in the series.
    """
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return sum_series(n - 1, first, second) + sum_series(n - 2, first, second)

