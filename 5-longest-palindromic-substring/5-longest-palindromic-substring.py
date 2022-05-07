class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return None
        result = ''
        maxPal = 0
        record = [[0] * len(s) for i in range(len(s))]
        for j in range(len(s)):
            for i in range(j+1):
                record[i][j] = ((s[i] == s[j]) and (j-i<=2 or record[i+1][j-1]))
                if record[i][j] and j-i+1 > maxPal:
                    maxPal = j-i+1
                    result = s[i:j+1]
        return result