class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        intNum1 = 0
        intNum2 = 0
        for i in num1:
            intNum1 = intNum1 * 10 + int(i)
        for i in num2:
            intNum2 = intNum2 * 10 + int(i)
        result = str(intNum1 + intNum2)
        return result