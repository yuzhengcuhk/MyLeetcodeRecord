class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        kSum = 0
        for i in range(0, k):
            kSum += nums[i]
        maxSum = kSum
        j = 0
        while (j+k < len(nums)):
            kSum += nums[j+k] - nums[j]
            maxSum = max(kSum, maxSum)
            j += 1
        return maxSum/k