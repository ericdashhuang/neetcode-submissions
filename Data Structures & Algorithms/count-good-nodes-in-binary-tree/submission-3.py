# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = deque(([root, root.val],))

        while q:
            node, curmax = q.pop()
            if node:
                if node.val >= curmax:
                    res += 1
                q.append((node.left, max(curmax, node.val)))
                q.append((node.right, max(curmax, node.val)))
        return res
                
