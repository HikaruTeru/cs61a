


a = 1                          # 全局帧：a -> 1

def f(g):
    a = 2                      # f 帧的局部绑定：a -> 2
    return lambda y: a * g(y)  # 返回一个新 lambda，捕获局部 a=2
                               #  λ₂ = lambda y: a * g(y)
result = f(lambda y: a + y)(a)      # λ₁ = lambda y: a + y
#           ^^^^^^^^^^^^^^^  ^
#        上级帧为 global , 调用时 a 取全局帧的值 1
         
         
higher_order_lambda = lambda f: lambda x: f(x)
g = lambda x: x * x
higher_order_lambda(2)(g) # 哪个参数属于哪个函数调用？

higher_order_lambda(g)(2)

