

def repeat(n):
    """返回一个装饰器，使被装饰函数重复执行 n 次"""
    def decorator(fn):
        def wrapped(x):
            for _ in range(n):
                fn(x)
        return wrapped
    return decorator

@repeat(3)          # repeat(3) 先被求值，返回 decorator
def greet(name):    # decorator(greet) 再被调用
    print(f"Hello, {name}")

greet("world")
# Hello, world
# Hello, world
# Hello, world


