"""
DESCRIPTION:
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution("abc", "bc") // returns true
solution("abc", "d") // returns false
"""
def solution(string, ending):
    z = len(string) - len(ending)
    if string[z:] == ending or ending == '' :
        return True
    return False