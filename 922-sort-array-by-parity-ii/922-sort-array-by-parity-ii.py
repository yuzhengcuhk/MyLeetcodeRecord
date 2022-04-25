class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        oddIndex = 1
        evenIndex = 0
        for item in nums:
            if item % 2 == 0:
                result[evenIndex] = item
                evenIndex += 2
            if item % 2 == 1:
                result[oddIndex] = item
                oddIndex += 2
        return result
            
                