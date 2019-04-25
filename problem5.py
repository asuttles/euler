primeFactor = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
sum = primeFactor

while True:

    # Check % for integers 1 to 20
    for i in range(1, 21):

        if sum % i != 0:        # Fail, next loop
            sum = sum + primeFactor
            break

    # Success: Number is factored by integers 1 to 20
    else:
        print("Answer = ", sum)
        break
