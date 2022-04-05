class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftIndex = 0
        rightIndex = len(nums) - 1
        while leftIndex <= rightIndex:
            midIndex = (leftIndex + rightIndex) // 2
            if target == nums[midIndex]:
                return midIndex
            elif target < nums[midIndex]:
                rightIndex = midIndex - 1
            elif target > nums[midIndex]:
                leftIndex = midIndex + 1
        return -1