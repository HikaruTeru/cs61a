
def make_adder(n):     # 外层函数，接收 n
    """返回一个将其参数与 n 相加的函数"""
    def adder(k):      # 内层函数，接收 k
        return k + n   # 用到了外层的 n
    return adder       # 返回内层函数对象本身（不是调用它,≠ adder() 的结果）
                       # make_adder返回一个函数 adder（可以被调用）


add_three = make_adder(3) # 等价于：add_three = 函数adder（n=3，k待定）
add_three(4)   # 返回 7

make_adder(1)(2)    # 返回 3
make_adder(2000)(26)  # 返回 2026




