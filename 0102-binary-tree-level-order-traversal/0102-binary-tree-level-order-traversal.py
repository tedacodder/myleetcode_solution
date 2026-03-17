# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque([root])
        ans=[]
        while q:
            length=len(q)
            res=[]
            for _ in range(length):
                value=q.popleft()
                if value:
                    res.append(value.val)
                if value and value.left:
                    q.append(value.left)
                if value and value.right:
                    q.append(value.right)
            if res:
                ans.append(res)
        return ans
        