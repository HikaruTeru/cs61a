
# Q5: Count Cond  Q5: 条件计数
def sum_digits(y):      # 各个位数的数字之和
    total = 0
    while y > 0:
        total, y = total + y % 10, y // 10
    return total

def is_prime(n):        # 判断一个数是否为质数
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

def count_fives(n):     # 计算 n×i 的数字和，判断是否等于 5, 并统计个数
    i = 1
    count = 0
    while i <= n:
        if sum_digits(n * i) == 5:
            count += 1
        i += 1
    return count

def count_primes(n):    # 统计 1 到 n 之间质数的个数
    i = 1
    count = 0
    while i <= n:
        if is_prime(i):
            count += 1
        i += 1
    return count

def count_cond(condition):
    def count(n):           # 返回一个接受 n 的函数
        i = 1
        total = 0
        while i <= n:
            if condition(n, i):   # 把 n 和 i 传给条件函数
                total += 1
            i += 1
        return total
    return count            # 返回函数本身，不是调用结果


