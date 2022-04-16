class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        result = []
        s1CountDict = collections.Counter(s1.split(' '))
        s2CountDict = collections.Counter(s2.split(' '))
        candidateSet = list((s1CountDict.keys() | s2CountDict.keys()) - (s1CountDict.keys() & s2CountDict.keys()))
        for item in candidateSet:
            if s1CountDict[item] == 1 or s2CountDict[item] == 1:
                result.append(item)
        return result