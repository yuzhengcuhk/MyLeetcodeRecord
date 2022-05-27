class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        N = len(nums)
        lastIndex= N - 1
        while lastIndex > 0 and nums[lastIndex] <= nums[lastIndex-1]:
            lastIndex -= 1
        if lastIndex == 0:
            nums.reverse()
            return
        leftIndex = lastIndex - 1
        rightIndex = N - 1
        while nums[rightIndex] <= nums[leftIndex]:
            rightIndex -= 1
        nums[leftIndex], nums[rightIndex] = nums[rightIndex], nums[leftIndex]
        leftIndex, rightIndex = leftIndex+1, N-1
        while leftIndex < rightIndex:
            nums[leftIndex], nums[rightIndex] = nums[rightIndex], nums[leftIndex]
            leftIndex, rightIndex = leftIndex+1, rightIndex-1