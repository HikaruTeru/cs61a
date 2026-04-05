
from math import sqrt

def has_big_sqrt(x):
    """判断 x 的实数平方根是否大于 10 """
    return x > 0 and sqrt(x) > 10

print(has_big_sqrt(1))       # False
print(has_big_sqrt(1000))    # True
print(has_big_sqrt(-10))   # False（x <= 0，右侧短路，不求值）


