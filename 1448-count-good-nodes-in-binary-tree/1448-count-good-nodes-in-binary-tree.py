# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        
        def dfs(node, max_node_val):
            nonlocal count
            
            if not node:
                return
            
            if node.val >= max_node_val:
                count += 1
            
            max_val = max(max_node_val, node.val)
            left = dfs(node.left, max_val)
            right = dfs(node.right, max_val)
            
        dfs(root,root.val)
            
            
        return count
            
            