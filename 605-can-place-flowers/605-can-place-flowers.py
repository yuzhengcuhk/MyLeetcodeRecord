class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        plotEmpty = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                if flowerbed[i] == 0:
                    plotEmpty += 1
                    flowerbed[i] = 1
        return plotEmpty >= n