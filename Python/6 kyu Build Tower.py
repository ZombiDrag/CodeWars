"""
DESCRIPTION:
Build Tower
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ", 
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]
Go challenge Build Tower Advanced once you have finished this :)
"""
def tower_builder(n_floors):
    z = []
    x = 1
    c = ((n_floors*2-1) // 2)
    for i in range(n_floors):
        if n_floors == 1:
            return ['*']
        z.append(' ' * c+(x*'*')+c * ' ')
        c-=1
        x+= 2
    return z