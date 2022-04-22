class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        leftIndex = 0
        rightIndex = len(nums) - 1
        while leftIndex < rightIndex:
            while leftIndex < rightIndex and nums[leftIndex] % 2 == 0:
                leftIndex += 1
            while leftIndex < rightIndex and nums[rightIndex] % 2 == 1:
                rightIndex -= 1
            swapTmp = nums[leftIndex]
            nums[leftIndex] = nums[rightIndex]
            nums[rightIndex] = swapTmp
        return nums