class Solution:
    def toHex(self, num: int) -> str:
        hexDict = {0:'0', 1:'1', 2:'2', 3:'3',
                   4:'4', 5:'5', 6:'6', 7:'7', 
                   8:'8', 9:'9', 10:'a', 11:'b', 
                   12:'c', 13:'d', 14 :'e', 15:'f'}  
        if num == 0:
            return("0")
        if num < 0:
            num = num + 2**32    
        result = ''
        while num > 0:
            result = result + hexDict[num%16]
            num = num // 16
        return result[::-1]