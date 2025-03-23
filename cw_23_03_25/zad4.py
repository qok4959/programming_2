def Fibonacci():
    a=0
    b=1
    while True:
        yield a
        temp=b
        b=a+b
        a=temp

obj = Fibonacci()
for _ in range(30):
    print(next(obj))