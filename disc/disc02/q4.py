
"""假设 find_digit(k) 已正确实现: 接收一个正整数 k 并返回一个函数 f, f 接收一个正整数 x 并返回 x 从右起第 k 位数字
如果 x 的位数少于 k, 则返回 0

实现 match_k: 接收一个整数 k 并返回一个函数。该函数接收变量 x, 如果 x 中所有相隔 k 位的数字都相同，则返回 True

"""
def match_k(k):
    """Returns a function that checks if digits k apart match.

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    def check(x):
        while x // (10 ** k) > 0:
            if ____________________________:
                return ____________________________
            x //= 10
        ____________________________
    ____________________________


