# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.treeArray = []
        self.treeInorder(root)
        return min(self.treeArray[i+1] - self.treeArray[i] for i in range(len(self.treeArray)-1))
        
    def treeInorder(self, root):
        if not root:
            return 
        self.treeInorder(root.left)
        self.treeArray.append(root.val)
        self.treeInorder(root.right)
        
        