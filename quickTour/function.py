def fibonacci(n):
    a,b = 0,1

    if(n==a):
        return a
    if(n==b):
        return b
    
    return fibonacci(n-1)+fibonacci(n-2)
    



for n in range(0,10):
    print(fibonacci(n))
