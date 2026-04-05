
from math import sqrt, pi

def area(r, shape_constant):
    """通用面积计算函数"""
    assert r > 0, 'A length must be positive'
    return r * r * shape_constant

def area_square(r):
    return area(r, 1)

def area_circle(r):
    return area(r, pi)

def area_hexagon(r):
    return area(r, 3 * sqrt(3) / 2)

# 测试
print(area_hexagon(10))    # 259.8...
print(area_hexagon(-10))   # AssertionError




