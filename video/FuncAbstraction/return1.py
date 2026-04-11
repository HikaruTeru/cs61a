
def print_until(n, d):
    """
    从个位起逆序打印 n 的各位数字，直到某位等于 d 为止（含该位）
    假设 n 为非负整数
    """
    while n > 0:
        last = n % 10       # 取个位数字
        n = n // 10         # 去掉个位
        print(last)
        if last == d:       # 命中目标数字，终止函数
            return None     # 显式返回 None，等价于直接 return


