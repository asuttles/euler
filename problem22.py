# Using names.txt, a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order.
#
# Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order,
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?
# ==============================================================================


# Sum of alphabetical positions in string
# (not case sensitive)
def getASCIIStringValue(bString):
    val = 0
    for char in bString.lower():
        val = val + int(char) - 96
    return val


# Read all names from file as byte string
f = open('names.txt', 'rb')
names = f.read()
f.close()

# Org names into sroted list of names
nameList = names.split(sep=b',')  # Split names into name list
nameList.sort()                   # Sort the name list

# Sum products of ascii value and index
total, i = 0, 1
for name in nameList:
    total += getASCIIStringValue(name.strip(b'"')) * i
    i += 1

print(total)
