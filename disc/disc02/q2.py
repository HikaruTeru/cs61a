
def make_keeper(n):
    """Returns a function that takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.
    实现 make_keeper 函数，它接收一个正整数 n 并返回一个函数 f
    该函数 f 接收另一个单参数函数 cond 作为参数。当调用 f(cond) 时，它会打印从 1 到 n (包含 n)之间
    所有满足条件的整数，即调用 cond(i) 返回真值的整数。每个整数打印在单独的一行。

    >>> def is_even(x): # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    >>> make_keeper(5)(lambda x: True)
    1
    2
    3
    4
    5
    >>> make_keeper(5)(lambda x: False)  # Nothing is printed
    """
    "*** YOUR CODE HERE ***"
    def f(cond):        # 不写 return 时，Python 会自动返回 None
        i = 1
        while i <= n:
            if cond(i) == True:
                print(i)
            i += 1 
    return f

    # return f 的含义："一个专门处理 n=__ 的函数，自行决定怎么用"