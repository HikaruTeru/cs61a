
def summation(n,term):
    total,k = 0,1
    while k <= n:
        total,k = total + term(k),k + 1
    return total

def natural(x):
    return x

def sum_natural(n):
    return summation(n,natural)

result = sum_natural(10)


>>> def summation(n, term):

>>> def summation(n, term):
        total, k = 0, 1
        while k <= n:
            total, k = total + term(k), k + 1
        return total

>>> def identity(x):
        return x

>>> def sum_naturals(n):
        return summation(n, identity)

>>> sum_naturals(10)
55

>>> summation(10, square)
385




def pi_term(x):
    return 8 / ((4*x-3) * (4*x-1))

def pi_sum(n):
    return summation(n, pi_term)

pi_sum(1e6)  # ≈ 3.14159...


