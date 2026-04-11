
def search(f):
    """
    寻找并返回最小的非负整数 x, 使得 f(x) 为真值。
    """
    x = 0
    while True:
        if f(x):
            return x
        x += 1

# 简化版实现
def search_short(f):
    x = 0
    while not f(x):
        x += 1
    return x


