class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        height = len(img)
        width  =  len(img[0])
        result = [[0 for i in range(width)] for j in range(height)]
        for y in range(height):
            for x in range(width):
                y_min = max(0, y-1)
                y_max = min(height-1, y+1)
                x_min = max(0, x-1)
                x_max = min(width-1, x+1)
                
                sumSmoother = 0
                for j in range(y_min, y_max+1):
                    sumSmoother += sum(img[j][x_min:x_max+1])
                    print(sumSmoother)
                result[y][x] = sumSmoother // (x_max-x_min+1) // (y_max-y_min+1) 
        return result
                