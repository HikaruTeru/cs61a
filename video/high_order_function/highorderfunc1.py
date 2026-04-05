
# 类型一：以函数为参数（本节重点）
def apply_twice(f, x):
    """将函数 f 对 x 应用两次"""
    return f(f(x))

print(apply_twice(cube, 2))   
# cube(cube(2)) = cube(8) = 512

# 类型二：以函数为返回值（后续课程内容）
def make_adder(n):
    """返回一个将输入加 n 的函数"""
    def adder(k):
        return k + n
    return adder

add5 = make_adder(5)
print(add5(3))   # 8

# 类型三：同时以函数为参数和返回值
def compose(f, g):
    """返回 f 与 g 的复合函数"""
    def composed(x):
        return f(g(x))
    return composed

square = lambda x: x * x
increment = lambda x: x + 1

square_then_increment = compose(increment, square)
print(square_then_increment(4))   
# increment(square(4)) = 17


