"""
DESCRIPTION:
ISBN-10 identifiers are ten digits long. The first nine characters are digits 0-9. The last digit can be 0-9 or X, to indicate a value of 10.

An ISBN-10 number is valid if the sum of the digits multiplied by their position modulo 11 equals zero.

For example:

ISBN     : 1 1 1 2 2 2 3 3 3  9
position : 1 2 3 4 5 6 7 8 9 10
This is a valid ISBN, because:

(1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0
Examples
1112223339   -->  true
111222333    -->  false
1112223339X  -->  false
1234554321   -->  true
1234512345   -->  false
048665088X   -->  true
X123456788   -->  false
"""

def valid_ISBN10(isbn): 
    z = 0
    c_position = 0
    print(len(isbn))
    if len(isbn) != 10:
        return False
    for i in isbn:
        
        c_position += 1
        print(f'{c_position}   ======  {10}')
        
        try:
            z += int(i) * c_position

        except ValueError:
            if isbn[-1:] == "X" and isbn[0] != "X" :  
                z += 10 * c_position
     
        
        
    print(f'{z}     {11}')
    if z % 11 == 0 and z != 0:
        
        
        return True
    else:
        return False