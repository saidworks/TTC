
n=int(input("enter a number"))
def factorial(n):
    factorial=1
    for i in range(1,n+1,1):
        factorial*=i
    return print(factorial)
factorial(n)
