
def end(n, d):
    while n > 0:
        last, n = n % 10, n // 10
        print(last)
        if last == d: 
            return None

def search(f):
    x = 0
    while True:           # 构造无限循环，依赖 return 退出
        if f(x):
            return x      # 找到满足条件的 x，返回并退出
        x += 1            # 否则尝试下一个整数

def search(f):
    x = 0
    while not f(x):       # 条件不满足时持续递增
        x += 1
    return x              # 退出循环时 f(x) 已为真值