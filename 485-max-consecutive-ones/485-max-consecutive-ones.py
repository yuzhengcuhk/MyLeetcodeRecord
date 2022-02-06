class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        numsString = (''.join([str(i) for i in nums])).split('0')
        maxString = max(numsString)
        return len(maxString)