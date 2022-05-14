class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        lenNums = len(nums)
        for startIndex in range(lenNums-2):
            if startIndex > 0 and nums[startIndex] == nums[startIndex-1]:
                continue
            leftIndex = startIndex + 1
            rightIndex = lenNums - 1
            while leftIndex < rightIndex:
                currSum = nums[startIndex] + nums[leftIndex] + nums[rightIndex] 
                if currSum == 0:
                    result.append([nums[startIndex], nums[leftIndex], nums[rightIndex]])
                    leftIndex += 1
                    rightIndex -= 1
                    while leftIndex < rightIndex and nums[leftIndex] == nums[leftIndex-1]:
                        leftIndex += 1
                    while leftIndex < rightIndex and nums[rightIndex] == nums[rightIndex+1]:
                        rightIndex -= 1
                elif currSum < 0:
                    leftIndex += 1
                else:
                    rightIndex -= 1
        return result