
def r(f):
    k = 2
    k, m = k + 1, f(k)
    return n

n = 10
g = (lambda n: lambda k: print(k * n))(-1)
r(g)

def r(f):
    k = 2
    k, m = k + 1, f(k)
    return n

n = 10

def outer(n):
    def inner(k):
        print(k * n)
    return outer

def r(f):
    k = 2
    k, m = k + 1, f(k)
    return n



"""
Frames              Objects
Global frame
    r
    n = 10

f1: λ [parent=Global]


    f2: λ [parent=f1]

"""

