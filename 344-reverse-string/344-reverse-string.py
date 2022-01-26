class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        index = 0
        jndex = len(s) - 1
        
        while index < jndex:
            tempValue = s[index]
            s[index] = s[jndex]
            s[jndex]= tempValue
            
            index += 1
            jndex -= 1
            