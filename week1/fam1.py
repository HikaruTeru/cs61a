
def improve(update, close, guess=1):
    """
    通用迭代改进框架
    update : 更新猜测值的函数，签名 update(guess) -> new_guess
    close  : 判断是否收敛的函数，签名 close(guess) -> bool
    guess  : 初始猜测值，默认为 1
    """
    while not close(guess):
        guess = update(guess)
    return guess




def golden_update(guess):
    return 1/guess + 1      # 性质1：黄金比例等于其倒数加 1

def square_close_to_successor(guess):
    # 性质2：黄金比例的平方等于其本身加 1
    return approx_eq(guess * guess, guess + 1)  # φ 满足 φ² = φ + 1

def approx_eq(x, y, tolerance=1e-15):
    """判断两个浮点数是否在给定容差范围内近似相等"""
    return abs(x - y) < tolerance



# 调用 improve 计算黄金比例近似值

phi_approx = improve(golden_update, square_close_to_successor)
# 输出：1.6180339887498951

# 用精确解验证结果

from math import sqrt
phi = 1/2 + sqrt(5)/2

def improve_test():
    approx_phi = improve(golden_update, square_close_to_successor)
    assert approx_eq(phi, approx_phi), 'phi differs from its approximation'

improve_test()  # 无异常则通过

