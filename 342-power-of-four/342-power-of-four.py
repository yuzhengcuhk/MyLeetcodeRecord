class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        while n:
            if n % 4 != 0:
                return False
            n = n // 4
            if n == 1:
                return True
            