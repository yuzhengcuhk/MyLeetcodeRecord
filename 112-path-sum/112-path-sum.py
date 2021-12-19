# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        li = []
        def pathsum(root, s):
            if not root:
                return 0
            s = s + root.val
            
            if not root.left and not root.right:
                li.append(s)
            
            left = pathsum(root.left, s)
            right = pathsum(root.right, s)
            return li
        
        pathsum(root, 0)
        if targetSum in li:
            return True
        else:
            return False
        
        
        
        