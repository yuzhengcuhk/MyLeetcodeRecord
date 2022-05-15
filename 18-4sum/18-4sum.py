class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        result = []
        startIndex = 0
        while startIndex < N - 3:
            secondIndex = startIndex + 1
            while secondIndex < N - 2:
                leftIndex = secondIndex + 1
                rightIndex = N - 1
                twoSum = target - nums[startIndex] - nums[secondIndex]
                while leftIndex < rightIndex:
                    if nums[leftIndex] + nums[rightIndex] > twoSum:
                        rightIndex -= 1
                    elif nums[leftIndex] + nums[rightIndex] < twoSum:
                        leftIndex += 1
                    else:
                        result.append([nums[startIndex], nums[secondIndex], nums[leftIndex], nums[rightIndex]])
                        while leftIndex < rightIndex and nums[leftIndex] == nums[leftIndex + 1]:
                            leftIndex += 1
                        while leftIndex < rightIndex and nums[rightIndex] == nums[rightIndex - 1]:
                            rightIndex -= 1
                        leftIndex += 1
                        rightIndex -= 1
                while secondIndex < N - 2 and nums[secondIndex] == nums[secondIndex + 1]:
                    secondIndex += 1
                secondIndex += 1
            while startIndex < N - 3 and nums[startIndex] == nums[startIndex + 1]:
                startIndex += 1
            startIndex += 1
        return result