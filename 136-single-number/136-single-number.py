class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        cnt = len(nums)
        
        if cnt == 1:
            return nums[0]
        
        if nums[0] != nums[1] and nums[1] == nums[2]:
            return nums[0]
        
        if nums[cnt-1] != nums[cnt-2] and nums[cnt-2] == nums[cnt-3]:
            return nums[cnt-1]
        
        for i in range(1, cnt-1):
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                return nums[i]
            