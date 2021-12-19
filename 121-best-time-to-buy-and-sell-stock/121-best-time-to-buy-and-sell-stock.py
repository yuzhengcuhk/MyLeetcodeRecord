class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        cnt = len(prices)
        maxProfit = 0
        minbuy = prices[0]
        
        for item in prices[1:]:
            if item < minbuy: 
                 minbuy = item
            elif item - minbuy > maxProfit:
                    maxProfit = item - minbuy
            else:
                continue
                    
        return maxProfit