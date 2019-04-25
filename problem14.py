# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Which starting number, under one million, produces the longest chain?


def nextN(num):
    if num % 2 == 0:
        return num / 2
    else:
        return 3 * num + 1


maxTerms, maxStartNum = 0, 0     # Record starting number for max terms

for i in range(1, 1000000):
    num, terms = i, 1

    while num > 1:
        num = nextN(num)
        terms += 1

    if terms > maxTerms:
        maxTerms = terms
        maxStartNum = i

print("The start number with the longest chain is ", maxStartNum)
print("This produces a sequence of length: ", maxTerms)
