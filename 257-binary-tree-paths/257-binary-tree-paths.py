# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        pathResult = []
        
        def pathTraverse(pathNode, pathNodeRecord):
            if pathNode != None:
                if pathNode.left == None and pathNode.right == None:
                    pathNodeRecord.append(str(pathNode.val))
                    pathNodeRecord = "->".join(pathNodeRecord)
                    pathResult.append(pathNodeRecord)
                else:
                    pathTraverse(pathNode.left, pathNodeRecord + [str(pathNode.val)])
                    pathTraverse(pathNode.right, pathNodeRecord + [str(pathNode.val)])
    
        pathTraverse(root, [])
        return pathResult