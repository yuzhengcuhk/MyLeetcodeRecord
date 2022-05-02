class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        leftIndex = 0
        rightIndex = len(nums) - 1
        result = [0] * len(nums)
        resultIndex = len(nums) - 1
        while leftIndex <= rightIndex:
            if nums[leftIndex] ** 2 > nums[rightIndex] ** 2:
                result[resultIndex] = nums[leftIndex] ** 2
                leftIndex += 1
                resultIndex -= 1
            else:
                result[resultIndex] = nums[rightIndex] ** 2
                rightIndex -= 1
                resultIndex -= 1
        return result