

def split_digit(n):
    """将数字拆分为‘除最后一位之外的部分’和‘最后一位’"""
    return n // 10, n % 10

def sum_digits(n):
    """计算整数 n 的各位数字之和 (用于处理翻倍后大于9的情况)"""
    if n < 10:
        return n
    else:
        all_but_last, last = split_digit(n)
        return sum_digits(all_but_last) + last

def luhn_sum(n):
    """
    处理不翻倍的位：
    计算 n 末位（不加倍），递归处理剩余部分时切换到加倍模式
    基准情况: 如果 n 为个位数，直接返回。
    递归情况: 保留最后一位，将其余部分传给 luhn_sum_double
    """
    if n < 10:
        return n
    last = n % 10
    rest = n // 10
    return luhn_sum_double(rest) + last

def luhn_sum_double(n):
    """
    计算 n 末位（加倍处理），递归处理剩余部分时切换回普通模式
    base case: n 为个位数，返回加倍后的各位数字和
    """
    last = n % 10
    luhn_digit = sum_digits(2 * last)  # 加倍，若>9则各位求和
    if n < 10:
        return luhn_digit
    rest = n // 10
    return luhn_sum(rest) + luhn_digit