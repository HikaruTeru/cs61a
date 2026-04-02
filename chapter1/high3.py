
def average(x, y):
    return (x + y) / 2  # 计算两数算术平均值，用于牛顿迭代法的更新步骤

def improve(update, close, guess=1):    # 通用迭代优化框架
    while not close(guess):
        guess = update(guess)  # 反复应用更新函数，直到满足收敛条件
    return guess

def approx_eq(x, y, tolerance=1e-3):    # 判断差值是否在容差范围内
    return abs(x - y) < tolerance       # 用作数值收敛的判断标准

def sqrt(a):        # 利用牛顿迭代法（巴比伦法）计算 a 的平方根
                    # sqrt_update 和 sqrt_close 通过词法作用域捕获参数 a
    def sqrt_update(x):
        return average(x, a / x)

    def sqrt_close(x):
        return approx_eq(x * x, a)

    # 将具体的更新策略和收敛策略注入通用迭代框架
    return improve(sqrt_update, sqrt_close)

result = sqrt(256)  # result = 16.0


