
"""
DESCRIPTION:
For this kata you will have to forget how to add two numbers.

It can be best explained using the following meme:
In simple terms, our method does not like the principle of carrying over numbers and just writes down every number it calculates :-)

You may assume both integers are positive integers.
Examples
     16         26        
   + 18       + 39            
   ------   -------   
    214        515

"""
def add(num1, num2):
    num_1_list = [int(i) for i in str(num1)]
    num_2_list = [int(i) for i in str(num2)]
    
    num_1_list =((len(num_2_list) - len(num_1_list))* [0,]) + num_1_list
    num_2_list = ((len(num_1_list) - len(num_2_list))* [0,]) + num_2_list
    
    num_sum_list = map(sum, zip(num_1_list,num_2_list))
    
    num_sum = int(''.join(map(str, num_sum_list)))
    return int(num_sum)