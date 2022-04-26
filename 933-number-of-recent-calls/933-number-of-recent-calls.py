class RecentCounter:

    def __init__(self):
        self.counter = []
        

    def ping(self, t: int) -> int:
        self.counter.append(t)
        currPosition = len(self.counter)
        prevPosition = bisect.bisect_left(self.counter, t-3000)
        return currPosition - prevPosition


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)