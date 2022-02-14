# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.lengthRecord = []
        self.treeTraverse(root)
        return max(self.lengthRecord)

        
    def treeTraverse(self, root):
        if not root:
            return 0
        leftLength = self.treeTraverse(root.left)
        rightLength = self.treeTraverse(root.right)
        self.lengthRecord.append(rightLength + leftLength)
        if rightLength > leftLength:
            return rightLength + 1
            
        else:
            return leftLength + 1
