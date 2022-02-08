class Solution:
    def convertToBase7(self, num: int) -> str:
        result = ""
        sign = ""
        index = 1
        if num == 0:
            return "0"
        if num < 0:
            num = abs(num)
            sign += "-"
        while num!=0:
            remainder = num % 7
            result += str(remainder)
            index += 1
            num = num // 7
        return sign + result[::-1]
         