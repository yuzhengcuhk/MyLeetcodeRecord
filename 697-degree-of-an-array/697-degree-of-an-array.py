class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        numPosition = {}
        frequenceRecord = {}
        maxDegree = 0
        for i in range(len(nums)):
            if nums[i] not in frequenceRecord:
                frequenceRecord[nums[i]] = 1     
            else:
                frequenceRecord[nums[i]] += 1
            if nums[i] not in numPosition:
                numPosition[nums[i]] = [i]
            else:
                numPosition[nums[i]].append(i)
            if frequenceRecord[nums[i]] > maxDegree:
                maxDegree = frequenceRecord[nums[i]]
        minLength = len(nums)
        for j in frequenceRecord:
            if frequenceRecord[j] == maxDegree:
                if numPosition[j][-1] - numPosition[j][0] + 1 <  minLength:
                    minLength = numPosition[j][-1] - numPosition[j][0] + 1 
        return minLength
            
 
        
                