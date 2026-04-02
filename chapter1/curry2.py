
def curry2(f):
    """将双参数函数 f 转换为柯里化形式"""
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

def uncurry2(g):
    """将柯里化函数 g 还原为双参数形式"""
    def f(x, y):
        return g(x)(y)
    return f

pow_curried = curry2(pow)
pow_curried(2)(5)        # 32
uncurry2(pow_curried)(2, 5)  # 32，还原后等价于 pow(2, 5)
