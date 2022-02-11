class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        countCapital = 0
        for itemChar in word:
            countCapital += int(itemChar.isupper())
        return countCapital == 0 or countCapital == len(word) or (countCapital == 1 and word[0].isupper())