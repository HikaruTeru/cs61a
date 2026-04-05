
def make_adder(n):
    def adder(k):
        return k + n
    return adder

print(adder) # error
print(adder(4)) # error
print(make_adder)
print(make_adder(4))
print(make_adder(2000)(26))
