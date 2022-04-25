class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        nameIndex = 0
        typedIndex = 0
        while nameIndex < len(name):
            tempCharacter = name[nameIndex]
            countCharacter = 0
            countType = 0
            while nameIndex < len(name) and name[nameIndex] == tempCharacter:
                countCharacter += 1
                nameIndex += 1
            while typedIndex < len(typed) and typed[typedIndex] == tempCharacter:
                countType += 1
                typedIndex += 1
            if countType < countCharacter:
                return False
            if nameIndex == len(name) and typedIndex < len(typed): # to process name = "alice" but typed = "aalliceex"
                while typedIndex < len(typed):
                    if typed[typedIndex] != name[nameIndex-1]:
                        return False
                    typedIndex += 1
        return True