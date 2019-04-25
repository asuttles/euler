def isPalindrome(x):

    x = str(x)                  # Convert x to a string
    i,j = 0,len(x)-1            # Search indices

    while i < j:
        
        if x[i] != x[j]:
            return False
        else:
            i += 1
            j -= 1
            
    return True


# Test 3-Digit Numbers
mxPal = 0,0,0

for i in range(100,1000):
    for j in range(i,1000):

        sum = i * j
        if isPalindrome(str(sum)) and sum > mxPal[0]:
            mxPal = sum,i,j


print("Max 3-digit Product Palindrome: ", mxPal[0],
      " is product of ", mxPal[1], " and ", mxPal[2])

