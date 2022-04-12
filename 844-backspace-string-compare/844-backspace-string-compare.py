class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        textS = ''
        textT = ''
        for item in s:
            if item == '#':
                if textS:
                    textS = textS[:-1]
            else:
                textS += item
        for item in t:
            if item == '#':
                if textT:
                    textT = textT[:-1]
            else:
                textT += item
        return textS == textT