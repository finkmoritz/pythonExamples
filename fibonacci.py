def fibo(n):
    if n in [0,1]:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

n = 3
print(str(n)+'th Fibonacci number = '+str(fibo(n))+'\n')


def fibonacci_numbers(max):
    a,b = 1,1
    while a < max:
        print(a)
        a,b = b,a+b

nMax = 10
print('Fibonacci numbers smaller than '+str(nMax)+':')
fibonacci_numbers(nMax)
