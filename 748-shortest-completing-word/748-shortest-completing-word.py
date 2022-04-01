class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        alphaPlate = ''.join([x for x in licensePlate if x.isalpha()]).lower()
        shortComplete = []
        countComplete = 0
        alphaPlateDict = Counter(alphaPlate)
        for item in words:
            if len(set(item)) < len(alphaPlateDict):
                continue
            countKey = 0        
            for key in alphaPlateDict:
                itemDict = Counter(item)
                if key not in item:
                    break
                if alphaPlateDict[key] > itemDict[key]:
                    break
                elif alphaPlateDict[key] <= itemDict[key]:
                    countKey += 1
            if countKey == len(alphaPlateDict):
                if not shortComplete:
                    shortComplete = [item]
                else:
                    if len(item) <  len(shortComplete[0]):
                        shortComplete = [item]
                        countComplete = 1
                    elif len(item) == len(shortComplete[0]):
                        shortComplete.append(item)
                        countComplete += 1
        return shortComplete[0]

                