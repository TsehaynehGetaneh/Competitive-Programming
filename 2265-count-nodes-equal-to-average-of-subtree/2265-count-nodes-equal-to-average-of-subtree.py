# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0
        
        def dfs(node):
            nonlocal count
            if not node:
                return (0,0)
            
            left_sum,left_count = dfs(node.left)
            right_sum,right_count = dfs(node.right)
            
            sum_ = node.val + left_sum + right_sum
            count_ = 1 + left_count + right_count
            
            
            if sum_//count_ == node.val:
                count += 1
                
            
            return sum_,count_
        
        dfs(root)
        
        return count
        
        
            
            
        