class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if (image[sr][sc] == newColor):
            return image
        self.DFSfloodFill(image, sr, sc, image[sr][sc], newColor)
        return image
    
    def DFSfloodFill(self, image, sr, sc, color, newColor):
        if (sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != color):
            return
        image[sr][sc] = newColor
        self.DFSfloodFill(image, sr - 1, sc, color, newColor)
        self.DFSfloodFill(image, sr + 1, sc, color, newColor)
        self.DFSfloodFill(image, sr, sc - 1, color, newColor)
        self.DFSfloodFill(image, sr, sc + 1, color, newColor)