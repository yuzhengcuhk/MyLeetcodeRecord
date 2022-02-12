# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.valueNodes = []
        self.treeTraverse(root)
        nodeDifference = []
        for nodeFirst, nodeSecond in zip(self.valueNodes, self.valueNodes[1:]):
            nodeDifference.append(nodeSecond - nodeFirst)
        return min(nodeDifference)
        
    
    def treeTraverse(self, node):
        if node.left:
            self.treeTraverse(node.left)
        self.valueNodes.append(node.val)
        if node.right:
            self.treeTraverse(node.right)
        