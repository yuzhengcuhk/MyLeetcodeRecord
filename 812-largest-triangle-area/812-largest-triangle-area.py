class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        result = 0
        lenList = len(points)
        for i in range(lenList-2):
            x1, y1 = points[i]
            for j in range(lenList-1):
                x2, y2 = points[j]
                for k in range(lenList):
                    x3, y3 = points[k]
                    result = max(result, 0.5 * abs((x2-x1) * (y3-y1) - (y2-y1) * (x3-x1))) 
                    # 0.5 * |P1 - P2| * | P2 - P3 | 
        return result
        