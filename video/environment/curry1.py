
def curry2(x):
    def g(x):
        def h(x):
            return x + y
        return h
    return g



def curry2(f):      # f 在这一层定义，接收函数 f
    def g(x):       # f 对 g 可见，接收第一个参数 x
        def h(y):   # f 对 h 也可见（闭包捕获），接收第二个参数 y
            return f(x, y)  # 所有参数就位，执行计算
        return h    # g 返回函数 h（尚未执行计算）
    return g        # curry2 返回函数 g（尚未执行计算）

curry2(add)(3)(5)

# 等价于：
(lambda f: lambda x: lambda y: f(x, y))(add)(3)(5)
#                                        ↑    ↑  ↑
#                                        f    x  y