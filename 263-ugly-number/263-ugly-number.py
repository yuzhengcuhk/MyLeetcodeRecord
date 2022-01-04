class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for factor in [30, 15, 10, 6, 5, 3, 2]:
            while n % factor == 0:
                n = n // factor
        
        if n == 1:
            return True
        else:
            return False