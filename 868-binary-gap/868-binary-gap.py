class Solution:
    def binaryGap(self, n: int) -> int:
        result, lastOne = 0, None
        for i in range(30): #10^9 -> 2^30
            if (n >> i) & 1:
                if lastOne is not None:
                    result = max(result, i-lastOne)
                lastOne = i
        return result
            