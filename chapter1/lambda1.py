

#     lambda           x           :         f(g(x))
"A function that   takes x   and returns    f(g(x))"
"一个函数，          接受 x      并返回       f(g(x))"

def compose1(f, g):
    return lambda x: f(g(x))

f = compose1(lambda x: x * x,
             lambda y: y + 1)
result = f(12)


s = lambda x: x * x
s(12)  # 144

# lambda 表达式可直接用于需要函数对象的位置
compose1 = lambda f, g: lambda x: f(g(x))



# 使用 def 定义，有名称，可读性更好
def compose1(f, g):
    return lambda x: f(g(x))

# 使用 lambda 全量表达，简洁但可读性差
compose1 = lambda f, g: lambda x: f(g(x))