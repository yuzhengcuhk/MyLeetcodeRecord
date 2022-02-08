# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        self.countMax = 0
        self.countMode = 0
        self.currentMode = root.val
        self.treeTraverse(root)
        return self.result
        
    def treeTraverse(self, root):
        if not root:
            return 
        self.treeTraverse(root.left)
        if root.val == self.currentMode:
            self.countMode += 1
        else:
            self.countMode = 1
        if self.countMode > self.countMax:
            self.countMax = self.countMode
            self.result = [root.val]
        elif self.countMode == self.countMax:
            self.result.append(root.val)
        self.currentMode = root.val
        self.treeTraverse(root.right)
        