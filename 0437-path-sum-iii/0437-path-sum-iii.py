# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        count = 0
        prefix_sum = 0
        
        def dfs(node):
            nonlocal count,dic,prefix_sum
            if not node:
                return
            
            prefix_sum += node.val
            if prefix_sum - targetSum in dic:
                count += dic[prefix_sum - targetSum]
                
            dic[prefix_sum] += 1
            
            dfs(node.left)
            dfs(node.right)
            
            dic[prefix_sum] -= 1
            prefix_sum -= node.val
            
            
        dfs(root)
        return count