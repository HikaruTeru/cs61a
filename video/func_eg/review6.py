

def remove_digit_alt(n, digit):
    kept = 0
    digits = 0
    while n > 0:
        last = n % 10
        n = n // 10
        if last != digit:
            kept += last / (10 ** (digits + 1))  # 以小数形式累加
            digits += 1
    return round(kept * (10 ** digits))           # 还原为整数


    