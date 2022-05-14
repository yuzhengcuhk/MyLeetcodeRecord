class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        sumClosest = math.inf
        lenNums = len(nums)
        result = None
        for startIndex in range(lenNums-2):
            leftIndex = startIndex + 1
            rightIndex = lenNums - 1
            while leftIndex < rightIndex:
                currSum = nums[startIndex] + nums[leftIndex] + nums[rightIndex]
                if abs(currSum - target) < sumClosest:
                    sumClosest = abs(currSum - target)
                    result = currSum
                if currSum > target:
                    rightIndex -= 1
                elif currSum <= target:
                    leftIndex += 1
        return result
