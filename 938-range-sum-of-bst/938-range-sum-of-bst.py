# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        result = 0
        if low <= root.val <= high:
            result += root.val
            result += self.rangeSumBST(root.left, low, high)
            result += self.rangeSumBST(root.right, low, high)
        elif root.val < low:
            result += self.rangeSumBST(root.right, low, high)
        else:
            result += self.rangeSumBST(root.left, low, high)
        return result