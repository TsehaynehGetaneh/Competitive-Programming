# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        ans = float("inf")
        
        def dfs(node,count):
            nonlocal ans
            if not node:
                return 0
            
            if not node.left and not node.right:
                ans = min(ans,count)
                # print(ans)
                
            dfs(node.left,count+1)
            dfs(node.right,count+1)
            
        dfs(root,1)
        
        return 0 if ans == float("inf") else ans
            
        
        
        