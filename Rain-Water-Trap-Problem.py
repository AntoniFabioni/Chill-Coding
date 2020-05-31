'''
Given some array of integers, each respresenting an elevation map of
rectangular hills of width one, how much many square units of water
would be trapped after it rains.
'''

def RainMeter(heights):
    
    total = 0
    bredth = len(heights)
    
    if bredth == 0:
        return total
    
    highLeft = [0]*(bredth + 1)

    for i in range(bredth):
        highLeft[i + 1] = max(highLeft[i], heights[i])
    
    highRight = 0

    for i in reversed(range(bredth - 1)):
        highRight = max(heights[i], highRight)
        total += min(highLeft[i], highRight) - heights[i] if min(highLeft[i], highRight) > heights[i] else 0
    
    return total

test = [0,-1,0,2,1,-1,-3,4,4,1,0,-2]

print(RainMeter(test))