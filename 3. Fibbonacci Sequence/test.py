def fib(n):
    a = 0
    b = 1

    print(a)    
    print(b)

    for i in range(2, n):
        print(a+b)
        a, b = b, a + b

fib(100000) #first seven nubers of Fibonacci sequence
