# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        nodeLCA = root
        while nodeLCA:
            if nodeLCA.val < p.val and nodeLCA.val < q.val:
                nodeLCA = nodeLCA.right
            if nodeLCA.val > p.val and nodeLCA.val > q.val:
                nodeLCA = nodeLCA.left
            else:
                return nodeLCA