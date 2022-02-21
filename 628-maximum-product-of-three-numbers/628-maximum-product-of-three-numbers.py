class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        Max2 = Max1 = nums[-1] * nums[-2] * nums[-3]
        if nums[0] < 0 and nums[1] < 0:
            Max2 = nums[0] * nums[1] * nums[-1]
        return max(Max1, Max2)
