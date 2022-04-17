class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        AliceSum = sum(aliceSizes)
        BobSum = sum(bobSizes)
        BobSet = set(bobSizes) # O(1) look-up for set, O(n) look-up for list
        swapTarget = (AliceSum + BobSum) // 2
        for item in aliceSizes:
            BobTarget = BobSum - swapTarget + item
            if BobTarget in bobSizes:
                return [item, BobTarget]
        return -1