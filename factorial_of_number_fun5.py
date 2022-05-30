def factorial(n):
    if n == 0:
        return 1
    else:
        p=1
        for i in range(1,n+1):
            p=p*i
        return p
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))
