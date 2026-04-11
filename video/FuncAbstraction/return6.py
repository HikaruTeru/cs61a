
def search(f):
    x = 0
    while True:
        if f(x):
            return x
        x += 1

def inverse(f):
    """返回 f 的逆函数（仅适用于结果为非负整数的情况）"""
    def g(y):
        return search(lambda x: f(x) == y)
    return g

def square(x):
    return x * x

sqrt = inverse(square)

