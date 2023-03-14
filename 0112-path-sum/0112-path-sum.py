# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        is_found = False

        def dfs(node,targetSum,sum_):
            nonlocal is_found
            if not node:
                return

            
            if not node.left and not node.right:
                sum_ += node.val

                if sum_ == targetSum:
                    is_found = True

            dfs(node.left,targetSum,sum_+node.val)
            dfs(node.right,targetSum,sum_+node.val)

        dfs(root,targetSum,0)
        
        return is_found
        
        
        