class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        incMon = False
        decMon = False
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                if incMon == False and decMon == True:
                    return False
                incMon = True
                decMon = False
            elif nums[i] < nums[i-1]:
                if incMon == True and decMon == False:
                    return False
                incMon = False
                decMon = True
            else:
                continue
        return True