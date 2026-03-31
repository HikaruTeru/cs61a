
# def 头部的 = ：声明默认值，不是赋值
def pressure(v, t, n=6.022e23):  # n=6.022e23 是默认值声明
    k = 1.38e-23           # k=1.38e-23 是赋值语句，将k绑定到局部帧
    return n * k * t / v

