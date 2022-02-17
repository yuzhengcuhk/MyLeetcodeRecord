# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:          
        return self.findSubRoot(root, subRoot)
        
    def findSubRoot(self, subroot1, subroot2):
        if subroot1:
            if subroot1.val == subroot2.val:
                possibleFlag = self.isSameTree(subroot1, subroot2)
                if possibleFlag:
                    return True
            return self.findSubRoot(subroot1.left, subroot2) or self.findSubRoot(subroot1.right, subroot2)
        return False
    
    def isSameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        elif (not root1 and root2) or (root1 and not root2) or (root1.val != root2.val):
            return False
        return self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)
        
    