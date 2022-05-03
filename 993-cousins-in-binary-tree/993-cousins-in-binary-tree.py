# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        levelNode = {}
        fatherNode = {}
    
        def isCousin(root, parent, count):
            if not root:
                return
            if count not in levelNode:
                levelNode[count] = []
            levelNode[count].append(root.val)
            if (root.val == x or root.val == y) and parent:
                fatherNode[root.val] = parent.val
            if x in levelNode[count] and y in levelNode[count] and fatherNode[x] != fatherNode[y]:
                return True
            return isCousin(root.left, root, count+1) or isCousin(root.right, root, count+1)
 
        return isCousin(root, None, 0)