class MyQueue:

    def __init__(self):
        self.queue = []
        self.behind = -1 
        self.front = -1

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.behind = self.behind + 1

    def pop(self) -> int:
        popResult = self.queue.pop(0)
        self.front = self.front + 1
        return popResult

    def peek(self) -> int:
        peekResult = self.queue[0]
        return peekResult
    
    def empty(self) -> bool:
        if self.behind == self.front:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()