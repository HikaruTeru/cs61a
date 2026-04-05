
def summation(n, term):
    """对 term(1) + term(2) + ... + term(n) 求和"""
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total
    

from operator import mul

def pi_term(k):
    return 8 / (mul(4*k - 3, 4*k - 1))

result = summation(1000000, pi_term)
# 输出约为 3.141592...