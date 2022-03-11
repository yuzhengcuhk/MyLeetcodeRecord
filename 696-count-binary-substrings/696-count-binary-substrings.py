class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        countResult = 0
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                countResult += 1
                leftIndex = i - 1
                rightIndex = i + 2
                while leftIndex >=0 and rightIndex < len(s):
                    if s[leftIndex] == s[leftIndex+1] and s[rightIndex] == s[rightIndex-1]:
                        countResult += 1
                        leftIndex -= 1
                        rightIndex += 1
                    else:
                        break
        return countResult
    