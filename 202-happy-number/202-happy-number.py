class Solution:
    def isHappy(self, n: int) -> bool:
        
        testSet = set()
        while n not in testSet:
            testSet.add(n)
            n = self.squreSum(n)
        
        return n == 1
        
    def squreSum(self, num: int) -> int:
        result = 0
        while num:
            remainder = num % 10
            result = result + remainder ** 2
            num = num // 10
        return result