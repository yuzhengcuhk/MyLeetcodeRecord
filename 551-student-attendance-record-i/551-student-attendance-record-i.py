class Solution:
    def checkRecord(self, s: str) -> bool:
        countAbsent = 0
        for i in range(len(s)):
            if s[i] == 'A':
                countAbsent += 1
                if countAbsent >=2:
                    return False
            if s[i] == 'L' and i < len(s)-2:
                if s[i+1] == 'L' and s[i+2]=='L':
                    return False
        return True
                