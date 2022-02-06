class Solution:
    def findComplement(self, num: int) -> int:
        result = 0
        binaryPlace = 1
        while num!=0:
            result += binaryPlace * ((num & 1)^1) # process last bit 
            binaryPlace *= 2                      # compute place value
            num //= 2                             # remove last bit
        return result