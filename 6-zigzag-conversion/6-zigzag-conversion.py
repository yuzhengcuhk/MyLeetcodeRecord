class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        result = ''
        for i in range(numRows):
            if i == 0 or i == numRows-1:
                result += self.addBoundary(s, numRows, i)
            else:
                result += self.addInner(s, numRows, i)
        return result
    
    def addBoundary(self, s, numRows, i):
        jumpTo = numRows * 2 - 2
        rowResult = ''
        while i < len(s):
            rowResult += s[i]
            i += jumpTo
        return rowResult
    
    def addInner(self, s, numRows, i):
        jumpTo1 = numRows * 2 - (i + 1) * 2
        jumpTo2 = numRows * 2 - 2
        rowResult = ''
        while i < len(s):
            rowResult += s[i]
            if i + jumpTo1 >= len(s):
                break
            rowResult += s[i + jumpTo1]
            i += jumpTo2
        return rowResult
        