# What is the index of the first term in the Fibonacci
# sequence to contain 1000 digits?

i  = 3
i2 = 1
i1 = 1


while(True):
    fib = i2 + i1
    if len( str(fib) ) == 1000:
        print( i )
        break
    else:
        i2 = i1
        i1 = fib
        i += 1
