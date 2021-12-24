class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numsSet = set(nums)
        if len(set(nums)) == len(nums):
            return False
        
        counter = len(nums)
        for i in range(counter):
            if len(nums[i:i+k+1]) != len(set(nums[i:i+k+1])):
                return True
            
        return False