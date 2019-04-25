def evenFibSum(limit):
    """Sum even Fib numbers below 'limit'"""

    sum = 0
    a,b = 1,2

    while b < limit:
        if b % 2 == 0:
            sum += b
        a,b = b,a+b

    return sum

"""By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms."""
print(evenFibSum(4000000))


