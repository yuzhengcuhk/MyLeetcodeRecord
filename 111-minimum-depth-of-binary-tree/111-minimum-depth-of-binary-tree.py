# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftwid = self.minDepth(root.left)
        rightwid = self.minDepth(root.right)
      
        if leftwid == 0:
            return rightwid + 1
        elif rightwid == 0:
            return leftwid + 1
        else:
            return min(leftwid, rightwid) + 1
        
            