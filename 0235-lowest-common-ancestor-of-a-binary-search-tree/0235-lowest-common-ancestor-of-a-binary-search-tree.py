# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traverse(node,p,q):
            if not node:
                return
            
            if (p.val > node.val) and (q.val > node.val):
                return traverse(node.right,p,q)
                
                
            if (p.val < node.val) and (q.val < node.val):
                return traverse(node.left,p,q)
            else:
                return node
            
            return traverse(node,p,q)
        
      
        
        return traverse(root,p,q)
        
        
        