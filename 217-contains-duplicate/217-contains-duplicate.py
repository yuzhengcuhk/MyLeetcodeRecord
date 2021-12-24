class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        numsBucket = {}
        counter = len(nums)
        for i in range(0, counter):
            if nums[i] in numsBucket:
                numsBucket[nums[i]] = numsBucket[nums[i]] + 1
                if numsBucket[nums[i]] >=2: 
                    return True
            else:
                numsBucket[nums[i]] = 1
                
        return False
                
        