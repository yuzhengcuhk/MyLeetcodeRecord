class Solution:
    def findLHS(self, nums: List[int]) -> int:
        numsDictionary = Counter(nums)
        numsSet = set(nums)
        result = 0
        for numItem in numsSet:
            if numItem+1 in numsSet:
                result = max(result, numsDictionary[numItem]+numsDictionary[numItem+1])
        return result