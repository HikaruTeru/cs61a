
higher_order_lambda = lambda f: lambda x: f(x)
g = lambda x: x * x
higher_order_lambda(2)(g) # 哪个参数属于哪个函数调用？

higher_order_lambda(g)(2)


def higher_order_lambda(f):
    def inner(x):
        return f(x)
    return inner

g = lambda x: x * x

"""
higher_order_lambda(2)
        ↓

higher_order_lambda(2)
        ↓
   f = 2         ← 把数字 2 当成函数传入
        ↓
返回 lambda x: 2(x)   ← 返回一个新函数

higher_order_lambda(2)(g)
        ↓
   x = g         ← 把 g 传给 x
        ↓
执行 2(g)         ← 尝试调用数字 2, 报错！


higher_order_lambda(g)
        ↓
   f = g         ← g 是函数 lambda x: x * x
        ↓
返回 lambda x: g(x)   ← 返回一个新函数

higher_order_lambda(g)(2)
        ↓
   x = 2         ← 把 2 传给 x
        ↓
执行 g(2)         ← 即 2 * 2
        ↓
返回 4

higher_order_lambda(g)(2)

第一次调用                 第二次调用
┌─────────────────┐       ┌─────────────────┐
│ f = g           │  →    │ x = 2           │
│ 返回lambda x:   │       │ 执行 f(x)        │
│     f(x)        │       │ = g(2)          │
└─────────────────┘       │ = 2 * 2 = 4     │
                          └─────────────────┘


>>> call_thrice = lambda f: lambda x: f(f(f(x)))
>>> call_thrice(lambda y: y + 1)(0)


def call_thrice(f):
    def λ(x):
        return f(f(f(x)))
    return λ


"""

print_lambda = lambda z: print(z)

def λ(z):
    return print(z)
