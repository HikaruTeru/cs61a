
def is_reasonable(n):
    """
    判断 n 是否为"合理数": 浮点数表示范围有限，极大的数会导致 1/n 被舍入为 0
    """
    return n == 0 or 1 / n != 0

print(is_reasonable(0))           # True（n == 0 为真，右侧短路）
print(is_reasonable(10))          # True（1/10 = 0.1 != 0）
print(is_reasonable(10 ** 100))   # True（1/10**100 仍为非零浮点数）
print(is_reasonable(10 ** 1000))  # False（1/10**1000 被舍入为 0.0）
print(is_reasonable(10 ** 10000)) # False（极大数，精度完全丢失）



