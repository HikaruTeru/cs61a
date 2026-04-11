
def square(x):
    return x * x

def triple(x):
    return x * 3

def compose1(f,g):
    def h(x):
        return f(g(x))
    return h


compose1(square, triple)(5)



