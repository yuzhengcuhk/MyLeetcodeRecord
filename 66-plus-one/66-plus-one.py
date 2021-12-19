class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        cnt = len(digits)
        if digits[cnt-1] != 9: 
            digits[cnt-1] = digits[cnt-1] + 1  
            return digits
        else:
            for i in range(0, len(digits)):
                digits[i] = str(digits[i])
            intdig = ''.join(digits)
            intdig = int(intdig) + 1
            result = []
            for item in str(intdig):
                result.append(int(item))
            return result