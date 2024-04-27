"""
DESCRIPTION:
A Narcissistic Number is a number of length l in which the sum of its digits to the power of l is equal to the original number. If this seems confusing, refer to the example below.

Ex: 153, where l = 3 ( the number of digits in 153 )
13 + 53 + 33 = 153

Write a function that, given n, returns whether or not n is a Narcissistic Number.
"""

def is_narcissistic(i):
    sum_x = 0
    list_x = []
    for x in str(i):
        list_x.append(x)
    for x in list_x:
        sum_x = sum_x+int(x)**len(str(i))
    return sum_x == i