class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        arrStr = ''.join(str(i) for i in num)
        arrInt = int(arrStr) + k
        return list(str(arrInt))