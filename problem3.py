from math import sqrt, ceil

def largestPrimeFactor(number):
    """Return largest prime factor of 'number'"""
    i = 2
    while i <= int(ceil(sqrt(number))):
        if number % i == 0:
            number //= i
            i = 2
        else:
            i += 1
    return number


print(largestPrimeFactor(600851475143))

