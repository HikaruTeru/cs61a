

def f(x):
    return g(x - 1)

def g(y):
    return h(y) - h(1 / y)

def h(z):
    return z ** 2   # 若漏写 return，函数隐式返回 None

print(f(12))

