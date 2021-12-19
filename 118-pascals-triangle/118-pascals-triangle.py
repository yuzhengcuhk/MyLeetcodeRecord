class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = []
        
        for i in range(1, numRows + 1):
            elementRow= [1] * i
            arr.append(elementRow)
        
        for j in range(1, numRows):
            for e in range(1, j):
                arr[j][e] = arr[j-1][e] + arr[j-1][e-1]
        
        return arr