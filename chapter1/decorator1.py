

# 装饰器语法
@trace
def triple(x):
    return 3 * x

# 等价的显式写法
def triple(x):
    return 3 * x
triple = trace(triple)  # triple 被重新绑定为 trace 的返回值



def trace(fn):
    """包装 fn, 在每次调用前打印函数名与参数"""
    def wrapped(x):
        print('-> ', fn, '(', x, ')')
        return fn(x)
    return wrapped

@trace
def triple(x):
    return 3 * x

triple(12)
# ->  <function triple at 0x102a39848> ( 12 )
# 36