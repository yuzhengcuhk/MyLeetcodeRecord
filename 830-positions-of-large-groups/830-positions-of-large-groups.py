class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        startIndex = 0
        endIndex = 0
        lenS = len(s)
        result = []
        while endIndex < lenS:
            while endIndex < lenS and s[startIndex] == s[endIndex]:
                endIndex += 1
            if endIndex - startIndex >= 3: 
                result.append([startIndex, endIndex-1])
            startIndex = endIndex 
        return result