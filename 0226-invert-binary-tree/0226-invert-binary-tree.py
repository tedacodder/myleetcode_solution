# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        head=root
        q=deque([head])

        while q:
            #swap the node
            value=q.popleft()
            if value.left:
                q.append(value.left)
            if value.right:
                q.append(value.right)
            value.left,value.right=value.right,value.left

        return root
