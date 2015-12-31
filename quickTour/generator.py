
def fibonacci(n):
    a,b = 0,1

    if(n==a):
        return a
    if(n==b):
        return b
    
    return fibonacci(n-1)+fibonacci(n-2)
         
def sumFibonacci(n):
   for i in range(0,n+1):
      yield fibonacci(i)


sum_of_fibonacci = sum(sumFibonacci(10))
print(sum_of_fibonacci)

