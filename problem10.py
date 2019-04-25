#
#  The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
#  Find the sum of all the primes below two million.
#

from problem7 import isPrime


sum, N = 0, 2000000

# Find the sum of primes below N
for i in range(2, N):
    if isPrime(i):
        sum += i
print("The sum of primes below N is: ", sum)
