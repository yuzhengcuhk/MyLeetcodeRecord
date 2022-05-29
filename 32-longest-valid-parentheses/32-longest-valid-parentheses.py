class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxValid = 0
        #From left to right
        leftIndex = 0
        rightIndex = 0
        for i in range(len(s)):
            if s[i] == '(':
                leftIndex += 1
            elif s[i] == ')':
                rightIndex += 1
            if leftIndex == rightIndex:
                maxValid = max(maxValid, 2 * leftIndex)
            elif rightIndex > leftIndex:
                leftIndex = 0
                rightIndex = 0
        #From right to left
        leftIndex = 0
        rightIndex = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '(':
                leftIndex += 1
            elif s[i] == ')':
                rightIndex += 1
            if leftIndex == rightIndex:
                maxValid = max(maxValid, 2 * leftIndex)
            elif rightIndex < leftIndex:
                leftIndex = 0
                rightIndex = 0
        return maxValid