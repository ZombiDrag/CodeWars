
"""
DESCRIPTION:
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
"""
def rot13(message):
    string = ''
    chars = "abcdefghijklmnopqrstuvwxyz"
    chars_up = chars.upper()
    x = 0
    
    
    for i in message:
        
        if chars_up.count(i) > 0:
            x = chars_up.index(i) + 13
            if x >= 26:
                x = x - 26
            i = chars_up[x]
        
        
        elif chars.count(i) > 0:
            x = chars.index(i) + 13
            if x >= 26:
                x = x - 26 
            i = chars[x]
        
        string += i
    
    return string