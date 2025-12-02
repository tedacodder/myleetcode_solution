# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def preorder(x):
            if x==None:
                return
            ans.append(x.val)
            preorder(x.left)
            preorder(x.right)
        
        preorder(root)
        return ans
        
        