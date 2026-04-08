
def apply_twice(f, x):
    """将函数 f 作用于 x 两次: f(f(x)) """
    return f(f(x))

def square(x):
    """计算 x 的平方 """
    return x * x

result = apply_twice(square, 2)


