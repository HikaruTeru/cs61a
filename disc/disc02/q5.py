
def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def ramp(n):
    """Return whether non-negative integer N has more increases than decreases.
    定义: 在一个非负整数中,如果左边的数字小于右边的数字,则两个相邻数字构成一个增加 increase
    如果左边的数字大于右边的数字, 则构成一个减少 decrease
    实现 ramp:接收一个非负整数 n,并返回在从左到右读取其数字时,其增加次数是否多于减少次数

    >>> ramp(123)   # 2 increases (1-> 2, 2-> 3) and 0 decreases
    True
    >>> ramp(1315)  # 2 increases (1-> 3, 1-> 5) and 1 decrease (3-> 1)
    True
    >>> ramp(176)   # 1 increase (1-> 7) and 1 decrease (7-> 6)
    False
    >>> ramp(5)     # 0 increases and 0 decreases
    False
    """
    n, last, tally = n // 10, n % 10, 0

    while n:
        n, last, tally = n // 10, n % 10, tally + sign(last - n % 10)
    return tally > 0