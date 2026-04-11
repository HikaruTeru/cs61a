
def search(f):
    x = 0
    while not f(x):
        x += 1
    return x
        

def is_three(x):
    return x == 3

search(is_three)   # 返回 3

def positive(f, x):
    """返回 max(0, f(x))，将负值截断为 0。"""
    return max(0, f(x))


def square(x):
    return x * x

def positive_square_minus_100(x):
    return max(0, square(x) - 100)

# positive_square_minus_100(10) == 0   （100 - 100 = 0，假值）
# positive_square_minus_100(11) == 21  （121 - 100 = 21，真值）

search(positive_square_minus_100)   # 返回 11



