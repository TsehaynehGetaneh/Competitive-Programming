# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        left,l = None,None
        def dfs(node,level):
            nonlocal left,l
            
            if not node:
                return 
            
            dfs(node.left,level+1)
            if (not left and not l) or level > l:
                l = level
                left = node.val
                
            dfs(node.right,level+1)
                
        dfs(root,0)
                
        return left
        