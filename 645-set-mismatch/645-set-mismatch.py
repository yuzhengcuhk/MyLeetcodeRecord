class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        sumCorrect = len(nums) * (len(nums) + 1) / 2
        numRepeat = sum(nums) - sum(set(nums))
        return [numRepeat, int(sumCorrect-sum(set(nums)))]