# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        leftValue = root.left.val if root.left else root.val
        rightValue = root.right.val if root.right else root.val
        if root.val != leftValue or root.val != rightValue:
            return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)