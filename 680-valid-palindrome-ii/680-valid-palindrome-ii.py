class Solution:
    def validPalindrome(self, s: str) -> bool:
        leftIndex = 0
        rightIndex = len(s) - 1
        while leftIndex < rightIndex:
            if s[leftIndex] != s[rightIndex]:
                sLeft = s[:leftIndex] + s[leftIndex+1:]
                sRight = s[:rightIndex] + s[rightIndex+1:]
                sInvLeft = sLeft[::-1]
                sInvRight = sRight[::-1]
                return sLeft == sInvLeft or sRight == sInvRight
            leftIndex += 1
            rightIndex -= 1
        return True
                
                