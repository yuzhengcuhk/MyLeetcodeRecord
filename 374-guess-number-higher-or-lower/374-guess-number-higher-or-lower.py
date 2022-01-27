# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lowNum = 1
        highNum = n
        pickFlag = None
        while lowNum <= highNum:
            midNum = (lowNum + highNum) // 2
            pickFlag = guess(midNum)
            if pickFlag == 0:
                return midNum
            elif pickFlag == -1:
                highNum = midNum - 1
            elif pickFlag == 1:
                lowNum = midNum + 1
        return "Error"