# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        left_tree = self.tree2str(root.left)
        right_tree = self.tree2str(root.right)
        
        
        if not left_tree and not right_tree:
            return str(root.val)
        
        elif not left_tree:
            return str(root.val) + "()" + "(" + right_tree + ")"
        
        elif not right_tree:
            return str(root.val) + "(" + left_tree + ")"
        else:
            return str(root.val) + "(" + left_tree + ")" + "(" + right_tree + ")"
            
        