
lambda x: x * x      # 单参数
lambda x, y: x + y   # 多参数
(lambda x: x * x)(5) # 直接作为调用表达式的运算符，返回 25



# 1. 绑定到变量名
square = lambda x: x * x
print(square(4))  # 输出 16

# 2. 立即调用 (Immediate Invocation)
result = (lambda x: x * x)(10)
print(result)     # 输出 100