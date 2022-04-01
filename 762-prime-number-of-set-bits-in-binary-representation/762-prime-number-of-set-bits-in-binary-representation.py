class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        countPrime = 0
        for item in range(left, right+1):
            leftBinary = bin(item)
            countOne = str(leftBinary).count('1')
            if countOne == 1:
                continue
            if countOne == 2:
                countPrime += 1
                continue
            else:
                primeFlag = 1
                for i in range(2, int(countOne ** 0.5) + 1):
                    if countOne % i == 0:
                        primeFlag = 0
                        break
                if primeFlag:
                    countPrime += 1
        return countPrime