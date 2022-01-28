class Solution:
    def longestPalindrome(self, s: str) -> int:
        sDict = Counter(s)
        result= 0
        flagOdd = False
        for key, value in sDict.items():
            if value % 2 == 0:
                result += value
            if value % 2 != 0:
                result += value - 1
                flagOdd = True
        if flagOdd:
            result = result + 1
        return result 