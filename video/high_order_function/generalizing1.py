
def sum_naturals(n):
    """求前 n 个自然数之和"""
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total

def sum_cubes(n):
    """求前 n 个自然数的立方和"""
    total, k = 0, 1
    while k <= n:
        total, k = total + pow(k, 3), k + 1
    return total

print(sum_naturals(5))   # 15
print(sum_cubes(5))      # 225

