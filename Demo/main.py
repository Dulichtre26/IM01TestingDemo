import math


def is_prime(n):
    if(n<2):
        return False
    for i in range(1,math.isqrt(n)+1):
        if n%i ==0:
            return False
    return True