class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        result = []
        leftIndex = 0
        rightIndex = n
        for i in range(n):
            if s[i] == 'I':
                result.append(leftIndex) 
                leftIndex += 1
            elif s[i] == 'D':
                result.append(rightIndex)
                rightIndex -= 1
        result.append(leftIndex)
        return result