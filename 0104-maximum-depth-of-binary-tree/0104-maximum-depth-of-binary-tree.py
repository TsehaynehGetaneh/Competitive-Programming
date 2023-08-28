# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        level_order = defaultdict(list)
        
        def traversal(level,node):
            if not node:
                return
            
            level_order[level].append(node.val)
            
            traversal(level+1,node.left)
            traversal(level+1,node.right)
            
        traversal(0,root)
        
        return len(level_order.keys())
        
        
        