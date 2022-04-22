# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.nodeArray = []
        self.treeTraverseInorder(root)
        if not self.nodeArray:
            return None
        newRoot = TreeNode(self.nodeArray[0])
        currNode = newRoot
        for i in range(1, len(self.nodeArray)):
            currNode.right = TreeNode(self.nodeArray[i])
            currNode = currNode.right
        return newRoot
        
    def treeTraverseInorder(self, root):
        if not root:
            return
        if root.left:
            self.treeTraverseInorder(root.left)
        self.nodeArray.append(root.val)
        if root.right:
            self.treeTraverseInorder(root.right)
        