class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = []
        heapq.heapify(self.minheap)
        for i in range(0, len(nums)):
            heapq.heappush(self.minheap, nums[i])
        
        while (len(self.minheap) > k):
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        while (len(self.minheap) > self.k):
            heapq.heappop(self.minheap)
        return self.minheap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)