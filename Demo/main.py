import math

def is_prime(n):
    if(n<2):
        raise ValueError('Invalid Input')
    for i in range(2,math.isqrt(n)+1):
        if n%i ==0:
            return False
    return True

def power(x,n):
    if n==0:
        return 1
    elif n>0:
        return x*pow(x,n-1)
    return power(x, n + 1) / x