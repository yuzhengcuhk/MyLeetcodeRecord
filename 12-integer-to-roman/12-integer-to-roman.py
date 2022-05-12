class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''
        numList = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romanList = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        for i in range(len(numList)):
            while num >= numList[i]:
                num -= numList[i]
                result += romanList[i]
        return result