class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []
        left, right, ans = n, n, []
        self.deepFirstSearch(left, right, ans, '')
        return ans
    
    def deepFirstSearch(self, left, right, ans, string):
        if left > right:
            return
        if not left and not right:
            ans.append(string)
        if left:
            self.deepFirstSearch(left-1, right, ans, string+'(')
        if right:
            self.deepFirstSearch(left, right-1, ans, string+')')
        