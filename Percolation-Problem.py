# An N-by-N grid has some proportion of cells "blocked", and the rest "open".
# The grid percolated if there is a contiguous path from the top row to the bottom row of open cells.
# The goal is to estimate the proportion that leads to near certain percolation.

import numpy as np

class Percolation:
    
    blocked = 0
    opened = 1
    full = 2

    def __init__(self, N):
        self.N = N
        self.total = N**2
        self.rows = [[Percolation.blocked]*N for row in range(N)]   #Creates N-by-N grid of blocked cells
    
    def open(self, x, y):
        self.rows[x][y] = Percolation.opened

    def isOpened(self, x, y):
        return self.open(x,y) == Percolation.opened

    def fill(self, x, y):
        self.rows[x][y] = Percolation.full

    def isFull(self, x, y):
        return self.open(x,y) == Percolation.full

    def percolates(self):
        '''
        Checks if any cells on the bottom row are full
        '''
        for y in range(self.N):
            if self.isFull(self.N - 1, y):
                return True
        return False

    def dfs(self, x, y):
        if x < 0 or x > self.N:
            return
        if y < 0 or y > self.N:
            return
        if not self.isOpened(x, y):
            return
        if self.isFull(x, y):
            return
        
        self.fill(x, y)

        self.dfs(x - 1, y)
        self.dfs(x + 1, y)
        self.dfs(x, y - 1)
        self.dfs(x, y + 1)

    # def neighborhood(self, x, y):
    #     '''
    #     Returns indices of cells adjacent to the one passed
    #     as an agument. Ignores cells outside of grid.
    #     '''
    #     nearby = []

    #     for xSum in range(x - 1, x + 2):
    #         if xSum == x or xSum < 0 or xSum > self.N - 1:
    #             continue     
    #         nearby.append([xSum, y])
            
    #     for ySum in range(y - 1, y + 2):
    #         if ySum == y or ySum < 0 or ySum > self.N - 1:
    #             continue        
    #         nearby.append([x, ySum])
            
    #     return nearby
        
    
    def countHoles(self):
        '''
        Counts how many cells are either opened or full
        '''
        return np.count_nonzero(self.rows)

# Test
fourbyfour = Percolation(4)
fourbyfour.open(1, 1)
fourbyfour.open(0, 3)