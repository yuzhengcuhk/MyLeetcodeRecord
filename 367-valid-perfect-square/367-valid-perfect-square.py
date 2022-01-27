class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lowNum = 1
        highNum = num
        while highNum >= lowNum:
            midNum = (lowNum + highNum) // 2
            if midNum ** 2 == num:
                return True
            elif midNum ** 2 > num:
                highNum = midNum - 1
            else:
                lowNum = midNum + 1
        return False