class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        My idea is to use bucket -> Passed
        
        sList = list(s)
        tList = list(t)
        sCounter = len(sList)
        tCounter = len(tList)
        if sCounter != tCounter:
            return False
        
        sBucket = {}
        for i in range(sCounter):
            if sList[i] in sBucket:
                sBucket[sList[i]] = sBucket[sList[i]] + 1
            else: 
                sBucket[sList[i]] = 1
                
        tBucket = {}
        for i in range(tCounter):
            if tList[i] in tBucket:
                tBucket[tList[i]] = tBucket[tList[i]] + 1
            else: 
                tBucket[tList[i]] = 1 
  
        return sBucket == tBucket
        """
        return Counter(s) == Counter(t)