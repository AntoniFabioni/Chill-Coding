# An N-by-N grid has some proportion of cells "blocked", and the rest "open".
# The grid percolated if there is a contiguous path from the top row to the bottom row of open cells.
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
    
    def open(self, row, col):
        self.rows[row][col] = Percolation.opened

    def isOpened(self, row, col):
        return self.rows[row][col] == Percolation.opened

    def fill(self, row, col):
        self.rows[row][col] = Percolation.full

    def isFull(self, row, col):
        return self.rows[row][col] == Percolation.full

    def percolates(self):
        '''
        Checks if any cells on the bottom row are full
        '''
        for col in range(self.N):
            if self.isFull(self.N - 1, col):
                return True
        return False

    def dfs(self, row, col):
        if not self.percolates():
            '''
            Acronym of "Depth-First Search"
            Ignores cells out of grid, blocked, or currently filled
            '''
            if row < 0 or row > self.N:
                return
            if col < 0 or col > self.N:
                return
            if not self.isOpened(row, col):
                return
            if self.isFull(row, col):
                return
            
            '''
            Fills the cell and its direct neighbours
            '''
            self.fill(row, col)

            self.dfs(row - 1, col)
            self.dfs(row + 1, col)
            self.dfs(row, col - 1)
            self.dfs(row, col + 1)
        
    def countHoles(self):
        '''
        Counts how many cells are either opened or full
        '''
        return np.count_nonzero(self.rows)

# Test

def simulate(N):
    '''
    Opens T random cells in an N-by-N grid
    '''
    grid = Percolation(N)
    options = list(range(grid.total))

    while not grid.percolates():
        randIndex = options.pop(random.randint(0, len(options) - 1))
        randCell = randIndex // grid.N, randIndex % grid.N

        grid.open(*randCell)
        grid.dfs(*randCell)

    return grid.countHoles()/grid.total


print(simulate(4))