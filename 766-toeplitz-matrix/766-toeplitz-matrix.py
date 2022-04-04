class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        width = len(matrix[0])
        height = len(matrix)
        for i in range(height-1):
            for j in range(width-1):
                if matrix[i+1][j+1] != matrix[i][j]:
                    return False
        return True
            