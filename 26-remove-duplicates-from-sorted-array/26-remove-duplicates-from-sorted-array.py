class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = j = 0
        cnt = len(nums)
        for i in range(0,cnt):
            if nums[j] != nums[i]:
                j = j + 1
                nums[j] = nums[i]
        return j+1    