class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n ^= (n>>1)
        return not (n & n+1)
            