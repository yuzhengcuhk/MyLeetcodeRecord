class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        for i, j in collections.Counter(nums).items():
            if j == n:
                return i
        return -1