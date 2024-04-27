"""
DESCRIPTION:
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
"""
def descending_order(num):  
    array = []
    x = None
    for i in str(num): 
        array.append(int(i))
    print(array)
    def sort(array):
        if len(array) < 2:
            return array
        else:
            number = array[0]
            end = [i for i in array[1:] if i >= number]
            start = [i for i in array[1:] if i < number]
            
            return sort(end) + [number] + sort(start)
    x = sort(array)
    answer = ''
    for i in x:
        answer += str(i)
    return int(answer)