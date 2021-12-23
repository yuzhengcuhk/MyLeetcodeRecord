class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        stMap = {}
        tsMap = {}
        counter = len(s)
        for i in range(counter):
            if s[i] not in stMap:
                stMap[s[i]] = t[i]
            if t[i] not in tsMap:
                tsMap[t[i]] = s[i]
            if stMap[s[i]] != t[i] or tsMap[t[i]] != s[i]:
                return False
            
        return True