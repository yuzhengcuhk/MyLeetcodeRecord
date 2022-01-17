class NumArray:

    def __init__(self, nums: List[int]):
        self.accumulateSum = [0]
        for i in range(len(nums)):
            currentSum = self.accumulateSum[-1] + nums[i]
            self.accumulateSum.append(currentSum)

    def sumRange(self, left: int, right: int) -> int:
        result = self.accumulateSum[right+1] - self.accumulateSum[left]
        return result

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)