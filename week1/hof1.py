

def summation(n, term):
    """
    计算 term(1) + term(2) + ... + term(n)
    n    : 上界
    term : 接受一个整数参数、返回数值的函数
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

# 以下为具体应用
def identity(x):
    return x

def cube(x):
    return x * x * x

def pi_term(x):
    return 8 / ((4*x-3) * (4*x-1))

# 调用示例
sum_naturals = lambda n: summation(n, identity)   # 自然数求和
sum_cubes    = lambda n: summation(n, cube)        # 立方和
pi_approx    = lambda n: summation(n, pi_term)     # π 的近似值



def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def cube(x):
    return x * x * x

def sum_cubes(n):
    return summation(n, cube)  # 将 cube 作为 term 传入

sum_cubes(3)  # 1 + 8 + 27 = 36





