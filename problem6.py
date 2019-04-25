# Diff  between sum of the squares of first hundred integers and the square of the sum
(lambda x: x*x)(sum(range(1,101))) - sum([n**2 for n in range(1,101)])

