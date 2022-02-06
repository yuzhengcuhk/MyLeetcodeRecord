class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        stringReverse = list(''.join(s.split('-')).upper())[::-1]
        counter = len(stringReverse)
        remainder = counter % k
        result = ''
        i = 0
        if remainder == 0:
            while i < counter-k+1:
                for j in range(k):
                    result += stringReverse[i+j]
                result += '-'
                i += k 
            finalResult = result[:-1]
        else:
            while i < counter:
                if i < (counter - remainder):
                    for j in range(k):
                        result += stringReverse[i+j] 
                    result += '-'
                    i += k 
                else:
                    result += stringReverse[i] 
                    i += 1
            finalResult = result
        return finalResult[::-1]
            