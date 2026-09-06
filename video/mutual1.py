
def split(n):               # 将一个整数拆分为两部分（最后一位 + 其它位）
    return n // 10, n % 10

def sum_digits(n):      # 递归计算一个整数各位数字之和
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum(n):        # 计算 Luhn 校验和
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):     # 处理偶数位:将末位数字翻倍
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        # 递归:前面部分回到 luhn_sum(奇数位), 加上当前处理过的偶数位
        return luhn_sum(all_but_last) + luhn_digit

def sum_digits_iter(n):
    digit_sum = 0
    while n > 0:
        n, last = n // 10, n % 10   # 拆分出最后一位
        digit_sum = digit_sum + last
    return digit_sum

def sum_digits_rec(n, digit_sum):
    if n == 0:                           # base case:循环条件的反面
        return digit_sum
    n, last = n // 10, n % 10            # 与循环体相同的拆分操作
    return sum_digits_rec(n, digit_sum + last)   # 用新值进行递归调用


def sum_digits(n):
    if n < 10:
        return n
    return sum_digits(n // 10) + n % 10

