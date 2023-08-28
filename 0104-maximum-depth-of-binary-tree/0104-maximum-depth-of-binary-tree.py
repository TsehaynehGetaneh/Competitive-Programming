# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def inorder(node):
            if not node:
                return 0
            
            left = 1 + inorder(node.left)
            right = 1 + inorder(node.right)
            
            return max(left,right)
        
        return inorder(root)
        
        
        