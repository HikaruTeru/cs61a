
def make_greeting(name):
    def greet():
        print(f"你好，{name}!")
    return greet

make_greeting("name")()
# 现在还没打印，稍后需要的时候再调用


