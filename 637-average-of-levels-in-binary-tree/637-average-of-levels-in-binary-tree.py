# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.levelSum = {}
        self.nodeCount = {}
        result = []
        self.treeTraverse(root, 0)
        for itemSum,itemCount in zip(self.levelSum.values(), self.nodeCount.values()):
            result.append(itemSum/itemCount)
        return result

    def treeTraverse(self, root, level):
        if root:
            if level in self.levelSum:
                self.levelSum[level] += root.val
                self.nodeCount[level] += 1
            else:
                self.levelSum[level] = root.val
                self.nodeCount[level] = 1
            self.treeTraverse(root.left, level+1)
            self.treeTraverse(root.right, level+1)
        