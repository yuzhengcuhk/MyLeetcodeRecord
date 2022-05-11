class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftIndex = 0
        rightIndex = len(height) - 1
        result = 0
        while leftIndex < rightIndex:
            result = max(result, min(height[leftIndex], height[rightIndex]) * (rightIndex -leftIndex))
            if height[leftIndex] < height[rightIndex]:
                leftIndex += 1
            elif height[leftIndex] >= height[rightIndex]:
                rightIndex -= 1
        return result