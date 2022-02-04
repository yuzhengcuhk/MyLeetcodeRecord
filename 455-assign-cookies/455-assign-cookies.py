class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        indexChild = 0
        for itemCookie in s:
            if itemCookie >= g[indexChild]:
                indexChild += 1 
                if indexChild > len(g) - 1:
                    break
        return indexChild 
            
            
                