# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        
        if (not root1 and root2) or (root1 and not root2) or (root1.val != root2.val):
            return False
        
        def dfs(node1,node2):
            if not node1 or not node2:
                return True
            
            if node1.left and node1.right:
                if node2.left and node2.right:
                    if node1.left.val == node2.left.val and node1.right.val == node2.right.val:
                        pass
                    elif node1.left.val == node2.right.val and node1.right.val == node2.left.val:
                        node1.left,node1.right = node1.right,node1.left
                    else:
                        return False
                else:
                    return False
                    
            elif node1.left:
                if (node2.left and node2.right):
                    return False
                elif node2.left and node2.left.val == node1.left.val:
                    pass
                
                elif node2.right and node2.right.val == node1.left.val:
                    node1.left,node1.right = node1.right,node1.left
                    
                else:
                    return False
                
            elif node1.right:
                if (node2.left and node2.right):
                    return False
                elif node2.right and node2.right.val == node1.right.val:
                    pass
                
                elif node2.left and node2.left.val == node1.right.val:
                    node1.left,node1.right = node1.right,node1.left
                    
                else:
                    return False
                    
            
            
            left = dfs(node1.left,node2.left)
            right = dfs(node1.right,node2.right)
            
            return left and right
        
        
        return dfs(root1,root2)
