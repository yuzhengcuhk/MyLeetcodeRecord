class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        result = 0
        for i in range(len(timeSeries)-1):
            if timeSeries[i] + duration > timeSeries[i+1]:
                result += timeSeries[i+1] - timeSeries[i]
            else:
                result += duration
        return result + duration