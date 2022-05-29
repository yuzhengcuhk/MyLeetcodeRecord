class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftIndex = 0
        rightIndex = len(nums) - 1
        while leftIndex <= rightIndex:
            midIndex = (leftIndex + rightIndex) // 2
            if nums[midIndex] == target:
                return midIndex
            if nums[midIndex] < nums[rightIndex]:
                if nums[midIndex] < target and nums[rightIndex] >= target:
                    leftIndex = midIndex + 1
                else:
                    rightIndex = midIndex - 1 
            else:
                if nums[midIndex] > target and target >= nums[leftIndex]:
                    rightIndex = midIndex - 1
                else:
                    leftIndex = midIndex + 1
        return -1 