class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        maxEat = len(candyType) // 2
        typeSet = set(candyType)
        if maxEat < len(typeSet):
            return maxEat
        else:
            return len(typeSet)