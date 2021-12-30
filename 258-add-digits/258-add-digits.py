class Solution:
    def addDigits(self, num: int) -> int:
        if not num:
            return 0
        numSum = 0
        while num:
            residue = num % 10
            numSum = numSum + residue
            num = num // 10
            if num == 0:
                if numSum < 10:
                    return numSum
                else:
                    num = numSum
                    numSum = 0
        
                