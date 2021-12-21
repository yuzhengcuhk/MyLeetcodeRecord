class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        listTitle = list(columnTitle)
        
        result = 0
        index = 0
        for item in reversed(listTitle):
            result = result + (ord(item) - 64) * (26 ** index)
            index = index + 1
        
        return result