class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        elif n < 1:
            return False
        else:
            while n!=1:
                if n % 3 != 0:
                    return False
                else:
                    n = n // 3
            return True