class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        countDeck = collections.Counter(deck)
        minX = min(countDeck.values())
        for x in range(2, minX + 1):
            if all(j % x == 0 for j in countDeck.values()):
                return True
        return False