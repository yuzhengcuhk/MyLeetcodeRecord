class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1,'V': 5,'X': 10, 'L': 50,'C': 100,'D': 500,'M': 1000}
        exception = {'IV': 4,'IX': 9,'XL': 40,'XC': 90,'CD': 400,'CM': 900}
        intnum = 0
        for exc in exception:
            if exc in s: 
                intnum = intnum + exception[exc]
                s = s.replace(exc, '')
        arr = list(s)
        for i in arr:
            intnum = intnum + roman[i]
        return intnum
