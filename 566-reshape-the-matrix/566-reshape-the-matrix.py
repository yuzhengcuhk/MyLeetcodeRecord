class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        numRow = len(mat)
        numColumn = len(mat[0])
        rowEach = 0  # to index the element of one row in previous matrix
        rowIndex = 0
        newMatrix = []
        if r * c != numRow * numColumn:  # Illegal case
            return mat
        while rowIndex < numRow:
            for i in range(r):
                newRow = []
                for j in range(c):
                    newRow.append(mat[rowIndex][rowEach]) 
                    rowEach += 1
                    if rowEach == numColumn:  # Next row in previous matrix
                        rowEach = 0
                        rowIndex += 1
                newMatrix.append(newRow)
        return newMatrix