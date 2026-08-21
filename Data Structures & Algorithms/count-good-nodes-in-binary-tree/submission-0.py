# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        # number of good nodes

        def dfs(node, curmax):
            nonlocal res
            if not node:
                return
            if node.val >= curmax:
                res += 1

            dfs(node.right, max(curmax, node.val))
            dfs(node.left, max(curmax, node.val))
        dfs(root, root.val)
        return res
