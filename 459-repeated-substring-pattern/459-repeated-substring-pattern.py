class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sLength = len(s)
        for i in range(1, sLength//2 + 1):
            if len(s) % i == 0:
                if (s[:i]) * int(sLength/i) == s:
                    return True
        return False