class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        xxmsum = nums[0]
        for index in range(1, len(nums)):
            xxmsum = max(nums[index], nums[index]+xxmsum)
            maxsum = max(maxsum, xxmsum)
        
        return maxsum
        

