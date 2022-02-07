class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstRow = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        secondRow = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        thirdRow = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        result = []
        for itemWord in words:
            if itemWord[0].lower() in firstRow:
                possibleRow = firstRow
            elif itemWord[0].lower() in secondRow:
                possibleRow = secondRow
            elif itemWord[0].lower() in thirdRow:
                possibleRow = thirdRow
            if self.isSameRow(itemWord, possibleRow):
                result.append(itemWord)
        return result
        
    def isSameRow(self, itemString: str, sameRow: list):
        for itemChar in itemString:
            if itemChar.lower() not in sameRow:
                return False
        return True