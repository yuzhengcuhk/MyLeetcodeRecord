class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sDict = Counter(s)
        tDict = Counter(t)
        
        for key in tDict:
            if key not in sDict or tDict[key] > sDict[key]:
                return key
        return None