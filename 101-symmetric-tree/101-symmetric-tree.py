# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isequal(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if (root1 is not None and root2 is None) or (root1 is None and root2 is not None):
            return False
        if root1.val == root2.val: 
            return self.isequal(root1.left, root2.right) and self.isequal(root1.right, root2.left) 
        if root1.val != root2.val:
            return False
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isequal(root.left, root.right)
    
    
        
        
