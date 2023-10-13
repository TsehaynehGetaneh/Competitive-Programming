# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,lb,ub):
            if not node:
                return True
            
            if node.val <= lb or node.val >= ub:
                return False
            
            check_left = dfs(node.left,lb,node.val)
            check_right = dfs(node.right,node.val,ub)
            
            return check_left and check_right
        
        return dfs(root,float("-inf"),float("inf"))
            
            
        