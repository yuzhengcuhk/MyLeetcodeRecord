class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        imageHeight = len(image)
        imageWidth = len(image[0])
        result = []
        for i in range(imageHeight):
            tempRow = []
            for j in range(imageWidth-1, -1, -1):
                if image[i][j] == 1:
                    tempRow.append(0)
                elif image[i][j] == 0:
                    tempRow.append(1)
            result.append(tempRow)
        return result