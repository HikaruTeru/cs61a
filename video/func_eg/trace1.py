
def trace1(fn):
    """
    接收一个单参数函数 fn, 返回一个在执行前会打印调用信息的函数。
    """
    def traced(x):
        print(f"Calling {fn.__name__} on argument {x}")
        return fn(x)
    return traced

# 基础函数
def square(n):
    return n * n

# 手动应用装饰逻辑（非语法糖方式）
square = trace1(square)

