# fibonacci numbers
# Formula (Fn = Fn1 + Fn2)

def fibonacci(num):
    Fn1 = 0
    Fn2 = 1
    for x in range(num):
        yield Fn1
        temp = Fn1
        Fn1 = Fn2
        Fn2 = temp + Fn2


for x in fibonacci(21):
    print(x)
