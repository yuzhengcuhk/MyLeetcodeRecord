# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.result1 = []
        self.result2 = []
        self.treeTraverse(root1, self.result1)
        self.treeTraverse(root2, self.result2)
        return self.result1 == self.result2
        
    def treeTraverse(self, root, record):
        if not root:
            return
        if not root.left and not root.right:
            record.append(root.val)
        if root.left:
            self.treeTraverse(root.left, record)
        if root.right:
            self.treeTraverse(root.right, record)