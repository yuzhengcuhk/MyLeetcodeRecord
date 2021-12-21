class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       
        majorBucket = {}
        counter = len(nums)
        
        for i in range(0, counter):
            if nums[i] in majorBucket:
                majorBucket[nums[i]] = majorBucket[nums[i]] + 1
            else:
                majorBucket[nums[i]] = 1
             
        resCounter = 0
        
        for key, value in majorBucket.items():
            if value > resCounter:
                result = key
                resCounter = value
        
        return result