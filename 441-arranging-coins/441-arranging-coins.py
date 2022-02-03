class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0 or n == 1:
            return n 
        coinRow = 1
        while n >= 0:
            n -= coinRow
            coinRow += 1
        return coinRow - 2