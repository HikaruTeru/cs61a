
def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)


def cascade(n):
    print(n)
    if n > 10:
        cascade(n // 10)
        print(n)


def cascade(n):
    """打印数字 n 的级联结构"""
    if n < 10:
        print(n)  # 基准情形
    else:
        print(n)            # 递归调用前的操作
        cascade(n // 10)    # 递归调用：传递去掉末位后的数值
        print(n)            # 递归调用后的操作