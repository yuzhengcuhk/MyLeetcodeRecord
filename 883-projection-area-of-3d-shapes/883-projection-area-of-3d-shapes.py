class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        topProject = 0
        frontProject = 0
        sideProject = 0
        for i in range(len(grid)):
            maxXProj = 0
            maxYProj = 0
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    topProject += 1
                maxXProj = max(maxXProj, grid[i][j])
                maxYProj = max(maxYProj, grid[j][i])
            frontProject += maxXProj
            sideProject += maxYProj
        return topProject + frontProject + sideProject
