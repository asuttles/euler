# ==============================================================================
# Let d(n) be defined as the sum of proper divisors of n
# (numbers less than n which divide evenly into n).
#
# If d(a) = b and d(b) = a, where a ≠ b,
# then a and b are an amicable pair and each of a and b are amicable numbers.
#
# For example, the proper divisors of 220 are:
# 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284.
#
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.
# ==============================================================================

numDict = {}                    # Number dictionary: i : d(i)


# Define d(n)
def d(x):
    divisors = []
    for i in range(1, x//2+1):
        if x % i == 0:
            divisors.append(i)
    return sum(divisors)


# Create Dictionary of sum of divisors
for i in range(1, 10001):
    numDict[i] = d(i)


# Scan dictionary for amicable numbers
amicableNumberList = []
for key, value in numDict.items():
    if (key != value) and (value in numDict.keys()):
        if numDict[value] == key:
            amicableNumberList.append(key)


# Print answer
print(sum(amicableNumberList))
