"""
DESCRIPTION:
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Examples
HighAndLow("1 2 3 4 5")  // return "5 1"
HighAndLow("1 2 -3 4 5") // return "5 -3"
HighAndLow("1 9 3 4 -5") // return "9 -5"
Notes
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
"""

def high_and_low(numbers):
    x = numbers.split(' ')
    x = list(map(int, x))
    x.sort()
    
    return f'{x[-1]} {x[0]}'