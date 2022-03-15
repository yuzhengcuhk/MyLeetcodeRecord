class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left, right+1):
            digitExtract = i % 10
            numi = i
            while numi != 0:
                if digitExtract == 0:
                    break
                if i % (digitExtract) != 0:
                    break
                else:
                    numi //= 10
                    digitExtract = numi % 10
                    if numi == 0:
                        result.append(i)
        return result