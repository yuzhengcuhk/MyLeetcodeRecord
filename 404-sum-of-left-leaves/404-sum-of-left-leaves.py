# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 0
        self.sumResult = 0
        def treeTraverse(root, flag):
            if not root:
                return None
            if not root.left and not root.right and flag == 'left':
                self.sumResult += root.val
            treeTraverse(root.left, 'left')
            treeTraverse(root.right, 'right')
        treeTraverse(root, 'root')
        return self.sumResult