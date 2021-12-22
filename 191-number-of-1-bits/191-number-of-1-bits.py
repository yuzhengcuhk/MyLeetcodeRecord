class Solution:
    def hammingWeight(self, n: int) -> int:
        
        result = 0
        
        while n:
            if n % 2 == 1:
                result = result + 1
                n = n // 2
            else:
                n = n // 2
        
        return result