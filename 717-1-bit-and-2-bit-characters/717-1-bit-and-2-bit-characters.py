class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        index = 0
        while index < len(bits):
            if bits[index] == 0 and index == len(bits)-1:
                return True
            if bits[index] == 1 and index == len(bits)-2:
                return False
            else:
                if bits[index] == 1:
                    index += 2
                else:
                    index += 1

        