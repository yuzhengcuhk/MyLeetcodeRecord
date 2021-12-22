class Solution:
    def reverseBits(self, n: int) -> int:
        
        nReverse = reversed(list(str(n)))
        index = 31
        result = 0
        while n:
            remainder = n % 2
            result = result + remainder * (2 ** index)
            index = index - 1
            n = n // 2
            
        return result