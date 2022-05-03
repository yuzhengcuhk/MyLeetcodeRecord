class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustRecord = [0] * (n+1)
        for i,j in trust:
            trustRecord[i] -= 1
            trustRecord[j] += 1
        for i in range(1, n+1):
            if trustRecord[i] == n-1:
                return i
        return -1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        