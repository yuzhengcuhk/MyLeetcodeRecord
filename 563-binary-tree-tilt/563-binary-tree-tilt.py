# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.tiltTree = [ ]
        self.treeTraverse(root)
        return sum(self.tiltTree)
    
    def treeTraverse(self, root):
        if not root:
            return 0
        tiltLeft = self.treeTraverse(root.left)
        tiltRight = self.treeTraverse(root.right)
        tiltNode = abs(tiltLeft - tiltRight)
        self.tiltTree.append(tiltNode)
        return tiltLeft + tiltRight + root.val