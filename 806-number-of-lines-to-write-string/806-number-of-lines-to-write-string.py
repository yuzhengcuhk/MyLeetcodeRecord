class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        if not widths:
            return [0, 0]
        lineCount = 1
        remainCount = 0
        for i in s:
            if remainCount + widths[ord(i) - 97] <= 100:
                remainCount += widths[ord(i) - 97]
            else:
                remainCount = widths[ord(i) - 97]
                lineCount += 1
        return [lineCount, remainCount]