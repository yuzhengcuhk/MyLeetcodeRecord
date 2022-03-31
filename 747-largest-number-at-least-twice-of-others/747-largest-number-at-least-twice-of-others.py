class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0
        sortNums = sorted(nums)[::-1]
        maxValue = sortNums[0]
        if maxValue < 2 * sortNums[1]:
            return -1
        else:
            return nums.index(maxValue)
        
            