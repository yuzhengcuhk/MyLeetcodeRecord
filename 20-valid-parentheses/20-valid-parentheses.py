class Solution:
    def isValid(self, s: str) -> bool:
        list = []
        cnt = len(s)
        for i in range(0, cnt):
            if s[i] in ['(','{','[']: 
                list.append(s[i])
            elif len(list) != 0: 
                if s[i] == ')' and list[-1] == '(':
                    list.pop()
                elif s[i] == '}' and list[-1] == '{':
                    list.pop()
                elif s[i] == ']' and list[-1] == '[':
                    list.pop()
                else:
                    list.append(s[i])
            else: 
                return False
        return len(list)==0 