class Solution:
    def isPalindrome(self, x: int) -> bool:
        arr = str(x)
        cnt = len(arr)
        for i in range(0,cnt):
            if arr[i] != arr[cnt-1-i]: 
                return 0 
        return 1    
            
        