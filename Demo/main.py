import math


def is_prime(n):
    if(n<2):
        return False
    for i in range(3,math.isqrt(n)+2):
        if n%i ==0:
            return False
    return True