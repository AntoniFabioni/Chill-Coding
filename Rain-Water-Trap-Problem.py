'''
Given some array of integers, each respresenting an elevation map of
rectangular hills of width one, how much many square units of water
would be trapped after it rains.
'''

def RainMeter(heights):
    
    # Total amount of water.
    total = 0

    # Width of the landscape, AKA the length of the array.
    bredth = len(heights)
    
    if bredth == 0:
        return total
    
    # Raises everything so that all elements are nonnegative.
    if min(heights) < 0:
        heights = [i - min(heights) for i in heights]

    highLeft = [0]*(bredth + 1)

    # Shows highest rectangle seen so far
    for i in range(bredth):
        highLeft[i + 1] = max(highLeft[i], heights[i])

    highRight = 0

    for i in range(bredth - 1, -1, -1):
        highRight = max(heights[i], highRight)
        total += min(highLeft[i], highRight) - heights[i] if min(highLeft[i], highRight) > heights[i] else 0
    
    return total

test = [0,-1,0,2,1,-1,-3,4]


print(RainMeter(test))