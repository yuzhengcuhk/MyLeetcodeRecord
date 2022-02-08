class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        for i in range(12):
            for j in range(60):
                if (bin(i)+bin(j)).count('1') == turnedOn:
                    result.append(str(i) + ":" + str(j).zfill(2))
        return result
