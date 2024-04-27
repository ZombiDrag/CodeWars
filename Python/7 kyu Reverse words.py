
"""
DESCRIPTION:
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"

"""
def reverse_words(text):
    a = text.split(' ')
    we = []
    for i in a:
        print(i[::-1])
        we.append(i[::-1])
    return ' '.join(we)