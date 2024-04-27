"""
DESCRIPTION:
For every good kata idea there seem to be quite a few bad ones!

In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.
"""
def well(x):
    y = 0
    s = 0
    for i in range(len(x)):
        if x[y] == 'good':
            y+=1
            s+=1
        else:
             y+=1
    if s > 2:
        return 'I smell a series!'
    elif s > 0:
        return 'Publish!'
    else:
        return 'Fail!'