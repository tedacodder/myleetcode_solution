# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def postorder(x):
            if x==None:
                return
            
            
            postorder(x.left)
            postorder(x.right)
            ans.append(x.val)
            
        
        postorder(root)
        return ans
        
        