class Solution:
    def countBits(self, n: int) -> List[int]:
        def bitCount(n):
            counter = 0
            while n!= 0: 
                if n%2 != 0:
                    counter = counter + 1
                n = n // 2
            return counter
        
        result = []
        for i in range(n+1):
            result.append(bitCount(i))
            
        return result