
# conflicting names
def compose1(f, g):     # 接收两个函数作为参数
    # h 的上层环境是 compose1 的局部帧，因此能正确捕获 f 和 g
    def h(x):           # 在内部定义一个新函数 h
        return f(g(x))  # h 的逻辑：先调用 g，再把结果传给 f
    return h            # 返回 h 这个函数本身（不是调用它）

def square(x):      # f(x) = x²
    return x * x

def successor(x):   # g(x) = x + 1
    return x + 1

def compose1(f, g):    # 高阶函数：接收2个函数作为参数，并返回一个新的函数
    def h(x):
        return f(g(x))
    return h

def f(x):
    """Never called."""
    return -x

# square_successor 是一个闭包，持有对 square 和 successor 的引用
square_successor = compose1(square, successor)
# 先执行 successor(12)=13，再执行 square(13)=169
result = square_successor(12)   


