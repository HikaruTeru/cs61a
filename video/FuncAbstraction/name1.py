
import math

# 不推荐：重复出现相同复杂表达式
if math.sqrt(a**2 + b**2) > threshold:
    result = math.sqrt(a**2 + b**2)

# 推荐：提取为具名变量，便于修改和阅读
hypotenuse = math.sqrt(a**2 + b**2)
if hypotenuse > threshold:
    result = hypotenuse


# 提取判别式，提升可读性
discriminant = b**2 - 4*a*c
x1 = (-b + math.sqrt(discriminant)) / (2*a)
x2 = (-b - math.sqrt(discriminant)) / (2*a)
