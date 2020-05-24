# An N-by-N grid has some proportion of cells "blocked", and the rest "open".
# The grid percolates if there is a contiguous path from the top row to the bottom row of open cells.
# The goal is to estimate the proportion that leads to near certain percolation.

import numpy as np
import random

class Percolation:
    
    blocked = 0
    opened = 1
    full = 2

    def __init__(self, N):
        self.N = N
        self.total = N**2
        self.rows = [[Percolation.blocked]*N for row in range(N)]   #Creates N-by-N grid of blocked cells

    def show(self):
        for row in self.rows:
            print(row)
    
    def inBounds(self, row, col):
        if row < 0 or row > self.N:
            return False
        elif col < 0 or col > self.N:
            return False
        else:
            return True
    
    def open(self, row, col):
        try:
            self.rows[row][col] = Percolation.opened
        except:
            pass
        #     print("(%d, %d) is out of bounds" % (row, col))

    def isOpened(self, row, col):
        try:
            return self.rows[row][col] == Percolation.opened
        except:
            pass
        #     print("(%d, %d) is out of bounds" % (row, col))

    def fill(self, row, col):
        try:
            self.rows[row][col] = Percolation.full
        except:
            pass
        #     print("(%d, %d) is out of bounds" % (row, col))

    def isFull(self, row, col):
        try:
            return self.rows[row][col] == Percolation.full
        except:
            pass
        #     print("(%d, %d) is out of bounds" % (row, col))

    def percolates(self):
        '''
        Checks if any cells on the bottom row are full
        '''
        for col in range(self.N):
            if self.isFull(self.N - 1, col):
                return True
        return False

    def dfs(self, row, col):
        '''
        Acronym of "Depth-First Search"
        Ignores cells out of grid, blocked, or currently filled
        '''
        if not self.inBounds(row, col):
            return
        if not self.isOpened(row, col) or self.isFull(row, col):
            return
        
        '''
        Fills the cell and its direct neighbours
        '''
        self.fill(row, col)

        self.dfs(row - 1, col)
        self.dfs(row + 1, col)
        self.dfs(row, col - 1)
        self.dfs(row, col + 1)
        
    def update(self, row, col):
        if row == 0:
            self.dfs(row, col)
        elif row != 0 and self.rows[row - 1][col] == Percolation.full:
            self.dfs(row, col)
        elif row != self.N - 1 and self.rows[row + 1][col] == Percolation.full:
            self.dfs(row, col)
        elif col != 0 and self.rows[row][col - 1] == Percolation.full:
            self.dfs(row, col)
        elif col != self.N - 1 and self.rows[row][col + 1] == Percolation.full:
            self.dfs(row, col)
    
    def countHoles(self):
        '''
        Counts how many cells are either opened or full
        '''
        return np.count_nonzero(self.rows)


def simulate(N):
    '''
    Simulates percolation on an N-by-N grid
    '''
    grid = Percolation(N)
    options = list(range(grid.total))

    while not grid.percolates():
        '''
        Choose a random blocked cell and open it
        '''
        randIndex = options.pop(random.randint(0, len(options) - 1))
        randCell = randIndex // grid.N, randIndex % grid.N

        grid.open(*randCell)
        grid.update(*randCell)

    return grid.countHoles()/grid.total

def demo(N):
    '''
    Visual of percolation on an N-by-N grid
    '''
    grid = Percolation(N)
    options = list(range(grid.total))

    while not grid.percolates():
        '''
        Choose a random blocked cell and open it
        '''
        randIndex = options.pop(random.randint(0, len(options) - 1))
        randCell = randIndex // grid.N, randIndex % grid.N

        grid.open(*randCell)
        grid.update(*randCell)

    grid.show()

trials = []
for i in range(100):
    trials.append(simulate(20))

print(np.mean(trials))

demo(8)