
def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    i , k = 0, 0
    while i < 10:
        if has_digit(n, i) == True:
            k = k + 1
        i = i + 1
    return k

def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    """
    记录原本的BUG
    while n // 10 > 0:
        if n % 10 == k or n // 10 == k:
            return True
        n = n // 10
    return False
    """
    while n > 0:
        if n % 10 == k:
            return True
        n = n // 10
    return False

