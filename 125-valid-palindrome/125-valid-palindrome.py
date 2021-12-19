class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ''.join(filter(str.isalnum, s)).lower()
        print(temp)
        return temp == temp[::-1]