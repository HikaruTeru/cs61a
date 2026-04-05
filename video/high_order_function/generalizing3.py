
def summation(n, term):
    """
    高阶函数：计算数列前 n 项之和
    n:    求和的项数上界
    term: 函数，接受索引 k, 返回第 k 项的值
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def identity(k):
    """恒等函数，返回 k 本身，用于自然数求和"""
    return k

def cube(k):
    """立方函数，返回 k 的三次方，用于立方和"""
    return pow(k, 3)

def pi_term(k):
    """莱布尼茨公式的第 k 项，级数收敛于 pi"""
    return 8 / ((4 * k - 3) * (4 * k - 1))


# 使用高阶函数 summation 重构特定求和函数
def sum_naturals(n):
    return summation(n, identity)

def sum_cubes(n):
    return summation(n, cube)

# 测试
print(sum_naturals(5))          # 15
print(sum_cubes(5))             # 225
print(summation(5, pi_term))    # 3.04...
print(summation(1000, pi_term)) # 趋近 π


