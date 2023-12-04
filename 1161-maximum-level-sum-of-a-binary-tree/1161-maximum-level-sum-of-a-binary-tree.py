# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_order_traversal = defaultdict(list)
        
        def dfs(node,level):
            if not node:
                return 
            
            level_order_traversal[level].append(node.val)
            
            left = dfs(node.left, level+1)
            right = dfs(node.right, level+1)
            
        dfs(root,1)
        
        max_sum = float("-inf")
        level = 1
        for key in level_order_traversal:
            summ = sum(level_order_traversal[key])
            if summ > max_sum:
                level = key
                max_sum = summ
                
        return level
            
            
        