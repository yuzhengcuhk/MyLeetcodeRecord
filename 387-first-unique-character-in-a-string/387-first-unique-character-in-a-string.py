class Solution:
    def firstUniqChar(self, s: str) -> int:
        strCounter = Counter(s)
        for key,value in strCounter.items():
            if value == 1:
                return s.index(key)
        return -1