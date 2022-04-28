class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0
        for i in range(len(strs[0])):
            column = [row[i] for row in strs]
            if column != sorted(column):
                result += 1
        return result