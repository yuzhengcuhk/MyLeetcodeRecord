class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        indexChangeFive = 0
        indexChangeTen = 0
        for item in bills:
            if item == 5:
                indexChangeFive += 1
            if item == 10:
                if indexChangeFive > 0:
                    indexChangeFive -= 1
                    indexChangeTen += 1
                else:
                    return False
            if item == 20:
                if indexChangeTen > 0:
                    indexChangeTen -= 1
                    if indexChangeFive > 0:
                        indexChangeFive -= 1
                    else:
                        return False
                else:
                    if indexChangeFive >=3:
                        indexChangeFive -= 3
                    else:
                        return False
        return True