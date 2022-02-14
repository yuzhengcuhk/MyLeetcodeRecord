class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) < k:
            return s[::-1]
        elif len(s) > k and len(s) < 2*k:
            reversePart = s[:k]
            remainPart  = s[k:]
            return reversePart[::-1] + remainPart
        else:
            result = ""
            for i in range(0, len(s), 2*k):
                result = result + s[i:i+k][::-1] + s[i+k:i+2*k] 
            return result