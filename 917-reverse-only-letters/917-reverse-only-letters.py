class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        leftIndex = 0
        rightIndex = len(s) - 1
        sList = list(s)
        while leftIndex < rightIndex:
            while leftIndex < rightIndex and not sList[leftIndex].isalpha():
                leftIndex += 1
            while leftIndex < rightIndex and not sList[rightIndex].isalpha():
                rightIndex -= 1
            sList[leftIndex], sList[rightIndex] = sList[rightIndex], sList[leftIndex]
            leftIndex += 1
            rightIndex -= 1
        return ''.join(sList)