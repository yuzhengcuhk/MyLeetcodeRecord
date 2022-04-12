class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        interSecX = min(rec1[3], rec2[3]) - max(rec1[1], rec2[1])
        interSecY = min(rec1[2], rec2[2]) - max(rec1[0], rec2[0])
        return interSecX > 0 and interSecY > 0