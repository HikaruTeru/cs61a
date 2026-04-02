
def curried_pow(x):
    def h(y):
        return pow(x, y)  # x 通过闭包从外层作用域捕获
    return h

curried_pow(2)(3)  # 等价于 pow(2, 3)，返回 8


def map_to_range(start, end, f):
    """对 [start, end) 范围内的每个整数调用 f 并打印结果"""
    while start < end:
        print(f(start))
        start = start + 1

# curried_pow(2) 返回一个单参数函数，符合 map_to_range 对 f 的接口要求
# 计算 2 的幂，依次输出 2º, 2¹, ..., 2⁹
map_to_range(0, 10, curried_pow(2))



