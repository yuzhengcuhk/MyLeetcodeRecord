class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        leftIndex = 0
        rightIndex = len(arr) - 1
        while leftIndex < rightIndex:
            midIndex = (leftIndex + rightIndex) // 2
            if arr[midIndex+1] < arr[midIndex] and arr[midIndex-1] < arr[midIndex]:
                return midIndex
            elif arr[midIndex+1] > arr[midIndex] and arr[midIndex-1] < arr[midIndex]:
                leftIndex = midIndex 
            elif arr[midIndex+1] < arr[midIndex] and arr[midIndex-1] > arr[midIndex]:
                rightIndex =  midIndex 
        return None
    # return arr.index(max(arr)) 