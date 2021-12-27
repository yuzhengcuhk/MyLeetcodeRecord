class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return None
        
        rangeResult = []
        counter = len(nums)
        index = 0
        while index < counter:
            j = index
            while j+1 < counter and nums[j+1] - nums[j] == 1:
                j = j + 1
            if j == index:
                rangeResult.append(str(nums[index]))
            else:
                rangeResult.append(str(nums[index]) + "->" + str(nums[j]))
            index = j + 1
            
        return rangeResult
        