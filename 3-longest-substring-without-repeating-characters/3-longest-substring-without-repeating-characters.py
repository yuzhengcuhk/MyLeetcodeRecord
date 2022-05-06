class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leftIndex = 0
        rightIndex = 0
        result = 0
        temSubstring = set()
        while leftIndex < len(s) and rightIndex < len(s):
            if s[rightIndex] in temSubstring:
                if s[leftIndex] in temSubstring:
                    temSubstring.remove(s[leftIndex])
                leftIndex += 1
            if s[rightIndex] not in temSubstring:
                temSubstring.add(s[rightIndex])
                rightIndex += 1
                result = max(result, len(temSubstring))
        return result