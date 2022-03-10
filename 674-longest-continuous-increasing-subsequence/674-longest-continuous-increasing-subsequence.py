class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maxIncLength = 1
        lengthCounter = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                lengthCounter += 1
                if lengthCounter > maxIncLength:
                    maxIncLength = lengthCounter
            else:
                lengthCounter = 1
        return maxIncLength