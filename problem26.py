# A unit fraction contains 1 in the numerator.
# The decimal representation of the unit fractions
#   with denominators 2 to 10 are given:
#
#    1/2	= 	0.5
#    1/3	= 	0.(3)
#    1/4	= 	0.25
#    1/5	= 	0.2
#    1/6	= 	0.1(6)
#    1/7	= 	0.(142857)
#    1/8	= 	0.125
#    1/9	= 	0.(1)
#    1/10	= 	0.1
#
# Where 0.1(6) means 0.166666..., and
# has a 1-digit recurring cycle.
#
# It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains
# the longest recurring cycle in its decimal fraction part.

maxLen = 0
maxNum = 0
print()


# for num in range(2,1000):
#     a = "{0:.2000f}".format(1/num)
#     a = a.lstrip("0.")              # Remove leading 0s and decimal
#
#     for i in range(1,1000):
#         x = a[0:i]
#         y = a[i:i+i]
#         if x == y:
#             print("Repeat: {0} 1/{0} = {1} (rpt len is: {2})".format(num,1/num,i))
#             if i > maxLen:
#                 maxLen = i
#                 maxNum = num
#             break
#
# print("MaxLen = ", maxLen)
# print("d = ", maxNum)


for num in range(2, 12):
    dividend = 10
    divisor = num
    quotient = dividend / divi
