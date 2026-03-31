
def summation(n,term):
    total,k = 0,1
    while k <= n:
        total,k = total + term(k),k+1
    return total

def cubes(x):
    return x*x*x

def sum_cubes(x):
    return summation(x,cubes)

result = sum_cubes(10)

