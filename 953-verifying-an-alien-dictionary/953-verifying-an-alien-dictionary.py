class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderDict = {c:i for i,c in enumerate(order)}
        for i in range(len(words)-1):
            if words[i] == words[i+1]:
                continue
            minLenWord = min(len(words[i]), len(words[i+1]))
            if len(words[i]) > len(words[i+1]) and words[i][:minLenWord] == words[i+1]:
                    return False
            for j in range(minLenWord):
                if orderDict[words[i][j]] < orderDict[words[i+1][j]]:
                    break
                elif orderDict[words[i][j]] > orderDict[words[i+1][j]]:
                    return False
                else:
                    continue
        return True
