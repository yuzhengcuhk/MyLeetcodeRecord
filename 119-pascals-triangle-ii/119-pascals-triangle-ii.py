class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = []
        for i in range(1, rowIndex+2):
            rowElement = [1] * i
            arr.append(rowElement)
            
        for j in range(2, rowIndex+1):
            for k in range(1, j):
                arr[j][k] = arr[j-1][k-1] + arr[j-1][k]
        
        return arr[rowIndex]
                
            