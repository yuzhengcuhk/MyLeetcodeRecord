class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        iNew = 0
        counter = len(nums)
        for i in range(counter):
            if nums[i] != 0:
                nums[iNew] = nums[i]
                iNew = iNew + 1
        
        for i in range(iNew, counter):
            nums[i] = 0
        
        