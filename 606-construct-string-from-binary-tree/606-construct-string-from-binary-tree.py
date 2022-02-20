# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return None
        self.result = ''
        self.treeTraverse(root)
        return self.result
    
    def treeTraverse(self, root):
        if not root:
            return '()'
        self.result += str(root.val)
        if root.left:
            self.result += '('
            self.treeTraverse(root.left)
            self.result += ')'
        elif root.right:
            self.result += '()'
        if root.right:
            self.result += '('
            self.treeTraverse(root.right)
            self.result += ')'
            