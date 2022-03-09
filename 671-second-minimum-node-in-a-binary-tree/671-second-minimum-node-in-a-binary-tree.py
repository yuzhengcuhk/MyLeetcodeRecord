# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.nodeRecord = []
        self.treeTraverse(root)
        minValue = min(self.nodeRecord)
        newNodeRecord = [value for value in self.nodeRecord if value != minValue]
        if newNodeRecord:
            return min(newNodeRecord)
        return -1
        
    def treeTraverse(self, root):
        if not root:
            return
        self.nodeRecord.append(root.val)
        self.treeTraverse(root.left)
        self.treeTraverse(root.right)
    