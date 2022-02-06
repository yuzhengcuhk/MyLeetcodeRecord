class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        widthMax = int(area**0.5)
        for recWidth in range(widthMax,1,-1):
            recLength = area // recWidth
            if recLength * recWidth == area:
                return [recLength, recWidth]
        return [area, 1]