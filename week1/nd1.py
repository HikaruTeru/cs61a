def sqrt(a):
        def sqrt_update(x):
            return average(x, a/x)
        def sqrt_close(x):
            return approx_eq(x * x, a)
        return improve(sqrt_update, sqrt_close)


def average(x, y):
    return (x + y) / 2

def approx_eq(x, y, tolerance=1e-3):
    return abs(x - y) < tolerance

def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def sqrt(a):
    # sqrt_update 和 sqrt_close 是局部函数，仅在 sqrt 的作用域内有效
    def sqrt_update(x):
        return average(x, a/x)   # 捕获了外层参数 a
    def sqrt_close(x):
        return approx_eq(x * x, a)  # 同样捕获了外层参数 a
    return improve(sqrt_update, sqrt_close)


