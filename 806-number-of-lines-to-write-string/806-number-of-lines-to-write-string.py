class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lineCount = 1
        remainCount = 0
        for i in s:
            iWidth = widths[ord(i) - 97] 
            if remainCount + iWidth <= 100:
                remainCount += iWidth
            else:
                remainCount = iWidth
                lineCount += 1
        return [lineCount, remainCount]