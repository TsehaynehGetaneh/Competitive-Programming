# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf_sq1 = []
        leaf_sq2 = []
        
        def dfs(node, is_tree1):
            if not node:
                return 
            
            if not node.left and not node.right:
                if is_tree1:
                    leaf_sq1.append(node.val)
                else:
                    leaf_sq2.append(node.val)
            
            dfs(node.left, is_tree1)
            dfs(node.right, is_tree1)
            
        # call dfs
        dfs(root1,True)
        dfs(root2,False)
        
        return leaf_sq1 == leaf_sq2
        