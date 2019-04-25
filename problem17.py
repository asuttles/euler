onesDict = {'0': 0,
            '1': 3,
            '2': 3,
            '3': 5,
            '4': 4,
            '5': 4,
            '6': 3,
            '7': 5,
            '8': 5,
            '9': 4,
            '10': 3,
            '11': 6,
            '12': 6,
            '13': 8,
            '14': 8,
            '15': 7,
            '16': 7,
            '17': 9,
            '18': 8,
            '19': 8}
tensDict = {'2': 6,
            '3': 6,
            '4': 5,
            '5': 5,
            '6': 5,
            '7': 7,
            '8': 6,
            '9': 6}
hundreds = 7
oneThousand = 11

sumLetters = 0

for i in range(1, 1001):
    number = str(i)

    # Handle One Thousand
    if len(number) > 3:
        sumLetters += oneThousand
        number = ''

    # Handle Hundreds
    if len(number) > 2:
        sumLetters += hundreds + onesDict[number[0]]
        number = number[1:]

        # Handle 'And'
        if int(number) > 0:
            sumLetters += 3

    # Handle Tens
    if len(number) > 1:
        if int(number) >= 20:
            sumLetters += tensDict[number[0]]
            number = number[1:]
        elif number[0] == '0':
            number = number[1:]
        else:
            sumLetters += onesDict[number]
            number = number[2:]
    # Handle Ones
    if len(number) > 0:
        sumLetters += onesDict[number]


print("The length of all number strings is: {0}".format(sumLetters))
