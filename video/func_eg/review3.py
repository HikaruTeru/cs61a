
def wrap(x):          # 外层函数，接收参数 x
    print("wait")      # 执行打印
    def inner():      # 在内部定义一个新函数
        return x      # inner 使用了外层的 x
    return inner      # 返回函数本身（不是调用它！）

wrap(10)()            # 调用方式





def delay(arg):
    print('delayed')
    def g():
        return arg
    return g

delay(delay)()(6)()



# delay(delay)()(6)

# delay(delay)()

# delay(delay)

# delay(delay)  