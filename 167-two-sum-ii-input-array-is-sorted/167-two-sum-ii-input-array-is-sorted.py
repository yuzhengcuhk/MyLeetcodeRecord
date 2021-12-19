class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cnt = len(numbers)
        
        i = 0
        j = cnt - 1
        
        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] > target:
                j = j - 1
            if numbers[i] + numbers[j] < target:
                i = i + 1
        
        return [i+1, j+1]