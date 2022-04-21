class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        result = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    result += grid[i][j] * 4 + 2
                if i != 0:
                    result -= min(grid[i][j], grid[i-1][j]) * 2 
                if j != 0:
                    result -= min(grid[i][j], grid[i][j-1]) * 2
        return result