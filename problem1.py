def natMult3and5(limit):
    """Find the sum of all the multiples of 3 or 5 below 'limit'"""

    sum = 0

    for i in range(limit):
        if i % 5 == 0 or i % 3 == 0:
            sum += i

    return sum

print(natMult3and5(1000))



