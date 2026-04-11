
def square(x):
    return x * x

def sum_squares(x, y):
    return square(x) + square(y)


# 实现一：使用乘法运算符
def square(x):
    return x * x

# 实现二：使用内置幂函数
def square(x):
    return pow(x, 2)

# 实现三：利用数学恒等式 (x-1)² + (2x-1) 展开的递推方式（非常规）
def square(x):
    return sum(range(1, 2*x, 2))  # 1+3+5+...+(2x-1) = x²

