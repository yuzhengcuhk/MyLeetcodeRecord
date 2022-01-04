class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsLen = len(nums)
        sumAll = numsLen * (numsLen + 1) // 2
        sumReal = sum(nums)
        return sumAll - sumReal