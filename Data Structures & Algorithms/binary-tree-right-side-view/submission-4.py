# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root]) if root else deque()
        res = []
        
        while q:
            rightview = None
            for i in range(len(q)):
                node = q.popleft()
                if i == 0:
                    rightview = node
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            if rightview:
                res.append(rightview.val)
    

        return res