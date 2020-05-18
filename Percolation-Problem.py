# An N-by-N grid has some proportion of boxes "blocked", and the rest "open".
# The grid percolated if there is a contiguous path from the top row to the bottom row of open boxes.
# The goal is to estimate the proportion that leads to near certain percolation.

class Percolation:

    def __init__(self, N):
        self.N = N
        self.rows = [[1]*N for i in range(N)]
    
    def open(self, x, y):
        self.rows[x][y] = 0

    def isOpen(self,x,y):
        return self.open(x,y) == 0
    
    def countOpen(self):
        return self.N**2 - sum([sum(i) for i in self.rows])     # Number of boxes minus sum of elements.
    


# Test
fivebyfive = Percolation(5)
fivebyfive.open(1,1)
print(fivebyfive.rows)
fivebyfive.open(0,4)
print(fivebyfive.isOpen(1,1))
print(fivebyfive.countOpen())