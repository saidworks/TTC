def fib(n):
    fibo = 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(9))
def fibonnaci(n):
    sum = [0,1]
    for i in range(2,n+1):
        sum.append(sum[-2]+sum[-1])
    return sum[n]
print(fibonnaci(9))


def Fib2(n):
    F = [0,1]
    for i in range(2,n+1):
        #compute F[i]
        F.append(F[-2] + F[-1])
    return F[n]
print(Fib2(9))