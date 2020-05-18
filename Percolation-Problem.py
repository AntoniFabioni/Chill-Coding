# An N-by-N grid has some proportion of boxes "blocked", and the rest "open".
# The grid percolated if there is a contiguous path from the top row to the bottom row of open boxes.
# The goal is to estimate the proportion that leads to near certain percolation.

class Percolation:

    def __init__(self, N):
        self.N = N
        self.rows = [[0]*N for i in range(N)]


# Test
fivebyfive = Percolation(5)
print(fivebyfive.rows)