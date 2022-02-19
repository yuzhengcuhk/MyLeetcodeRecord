class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        minRow = math.inf
        minColumn = math.inf
        for element in ops:
            minRow = min(minRow, element[0])
            minColumn = min(minColumn, element[1])
        return minRow * minColumn