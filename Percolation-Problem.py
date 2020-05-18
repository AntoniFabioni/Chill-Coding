# An N-by-N grid has some proportion of cells "blocked", and the rest "open".
# The grid percolated if there is a contiguous path from the top row to the bottom row of open cells.
# The goal is to estimate the proportion that leads to near certain percolation.

class Percolation:

    def __init__(self, N):
        self.N = N
        self.total = N**2
        self.rows = [[1]*N for i in range(N)]
    
    def open(self, x, y):
        self.rows[x][y] = 0

    def isOpen(self, x, y):
        return self.open(x,y) == 0

    def neighborhood(self, x, y):
        '''
        Returns indices of cells adjacent to the one passed
        as an agument. Ignores cells outside of grid.
        '''
        nearby = []

        for xSum in range(x - 1, x + 2):
            if xSum == x or xSum < 0 or xSum > self.N - 1:
                continue     
            nearby.append([xSum, y])
            
        for ySum in range(y - 1, y + 2):
            if ySum == y or ySum < 0 or ySum > self.N - 1:
                continue        
            nearby.append([x, ySum])
            
        return nearby
        
    
    def countOpen(self):
        '''
        Number of cells minus sum of elements.
        '''
        return self.total - sum([sum(i) for i in self.rows])
    


# Test
fivebyfive = Percolation(4)
fivebyfive.open(1, 1)
fivebyfive.open(0, 3)
print(fivebyfive.rows)
print(fivebyfive.neighborhood(3, 2))