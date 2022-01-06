class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pList = list(pattern)
        sList = s.split(" ")
        
        if len(pList) != len(sList):
            return False
        
        psMap = {}
        spMap = {}
        
        for i in range(len(pList)):
            if pList[i] not in psMap:
                psMap[pList[i]] = sList[i]
            if sList[i] not in spMap:
                spMap[sList[i]] = pList[i]
            if spMap[sList[i]] != pList[i] or psMap[pList[i]] != sList[i]:
                return False
        return True
        
