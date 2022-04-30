class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        fib0 = 0
        fib1 = 1
        for i in range(2, n+1):
            fibn = fib0 + fib1
            fib0 = fib1
            fib1 = fibn
        return fibn
            