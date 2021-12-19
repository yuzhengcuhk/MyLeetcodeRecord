class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        start = 1
        mid = 2
        for i in range(3, n+1):
            end = start + mid
            start = mid
            mid = end
        return mid 
        