# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node: Optional[Treenode], min: int, max: int):
            if not node:
                return True
            
            if min < node.val < max:
                return dfs(node.left, min, node.val) and dfs(node.right, node.val, max)
            else:
                return False
        return dfs(root, -float('inf'), float('inf'))


