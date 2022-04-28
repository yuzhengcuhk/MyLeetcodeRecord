class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        maxIndex = arr.index(max(arr))
        if not 0 < maxIndex < len(arr) - 1:
            return False
        for i in range(0, maxIndex):
            if arr[i] >= arr[i+1]:
                return False
        for j in range(maxIndex, len(arr)-1):
            if arr[j+1] >= arr[j]:
                return False
        return True