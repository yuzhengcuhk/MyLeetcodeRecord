class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        current = columnNumber
        while current:
            residual = current % 26
            if residual==0:
                result = chr(90) + result
                current = current - 26
            else:
                result = chr(residual+64) + result
            
            if current - residual> 0:
                    current = (current - residual) // 26 
            else:
                break
      
        return result
        

        