class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        countIndex = 0
        for matchIndex in t:
            if countIndex == len(s) - 1 and s[countIndex] == matchIndex:
                return True
            if s[countIndex] == matchIndex:
                countIndex += 1
        return False