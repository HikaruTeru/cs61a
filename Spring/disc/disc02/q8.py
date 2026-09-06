def every(t):
    """Return a function that returns whether t is True 
    for every digit of non-negative n.

    >>> f = every(lambda d: d % 2 == 1)
    >>> f(37511)  # every digit is odd
    True
    >>> f(2023)   # Not every digit is odd
    False
    """
    def digit(n):
        while n:
            if ____________________________:
                ____________________________
            n = n // 10
        return ___________________________
    return ___________________________
