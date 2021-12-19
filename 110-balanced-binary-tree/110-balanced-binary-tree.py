# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        else:
            lefth=self.height(root.left)
            righth=self.height(root.right)
            if lefth - righth > 1 or righth - lefth > 1:
                return False
            leftbal = self.isBalanced(root.left)
            rightbal = self.isBalanced(root.right)
            if leftbal and rightbal:
                return True
            else:
                return False
            
            
            
    def height(self, root):
        if root is None:
            return 0
        else:
            left = self.height(root.left)
            right = self.height(root.right)
            return 1 + max(left, right)
            