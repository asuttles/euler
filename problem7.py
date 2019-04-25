import math


def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


if __name__ == "__main__":
    i, counter = 1, 0
    while counter < 10001:
        i += 1
        if isPrime(i):
            counter += 1
    print("The 10,001st prime number is ->: ", i)
