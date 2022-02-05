class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.rowLength = len(grid)
        self.colLength = len(grid[0])
        result = 0
        if self.rowLength == 0 or self.colLength == 0:
            return 0
        for i in range(0, self.rowLength):
            for j in range(0, self.colLength):
                if (grid[i][j]) == 1:
                    result +=4                        # one grid cell with four perimeters
                    if (self.isShared(grid, i+1, j)): # right neighbor
                        result -=1
                    if (self.isShared(grid, i-1, j)): # left neighbor
                        result -=1
                    if (self.isShared(grid, i, j-1)): # up neighbor
                        result -=1
                    if (self.isShared(grid, i, j+1)): # down neighbor
                        result -=1
        return result
    
    def isShared(self, grid, rowNeighbor, colNeighbor):
        if rowNeighbor < 0 or rowNeighbor >= self.rowLength or colNeighbor < 0 or colNeighbor >= self.colLength: 
            return False                              # out of bound
        if grid[rowNeighbor][colNeighbor] == 1:
            return True
        return False