class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        leftIndex = 0
        rightIndex = len(nums) - 1
        if  target not in nums:
            return [-1, -1]
        while nums[leftIndex] < nums[rightIndex]:
            midIndex = (leftIndex + rightIndex) // 2
            if nums[midIndex] > target:
                rightIndex = midIndex - 1
            if nums[midIndex] < target:
                leftIndex = midIndex + 1
            if nums[midIndex] == target:
                if nums[rightIndex] > target:
                    rightIndex -= 1
                if nums[leftIndex] <target:
                    leftIndex += 1
        return [leftIndex, rightIndex] 