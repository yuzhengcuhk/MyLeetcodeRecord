class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        slowIndex = cost[0]
        quickIndex = cost[1]
        for i in range(2, len(cost)):
            slowIndex, quickIndex = quickIndex, min(slowIndex, quickIndex) + cost[i]
        return min(slowIndex, quickIndex)