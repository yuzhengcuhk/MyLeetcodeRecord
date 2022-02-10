class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        threePrize = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        scoreSort = reversed(sorted(score))
        countScore = len(score)
        result=  []
        scoreMapPlace = {}
        for index, itemScore in enumerate(scoreSort):
            if index >= 3:
                scoreMapPlace[itemScore] = str(index+1)
            else:
                scoreMapPlace[itemScore] = threePrize[index]
        for i in range(countScore):
            result.insert(i, scoreMapPlace[score[i]])
        return result