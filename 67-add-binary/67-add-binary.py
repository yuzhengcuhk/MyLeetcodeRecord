class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        result = a + b
        result = bin(result)
        return (result[2:])