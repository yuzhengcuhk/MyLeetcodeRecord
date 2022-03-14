class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumNums = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            rightSum = sumNums - nums[i] - leftSum
            if rightSum == leftSum:
                return i
            else:
                leftSum += nums[i]
        return -1