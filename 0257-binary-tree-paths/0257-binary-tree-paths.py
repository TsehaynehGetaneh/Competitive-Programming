# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        output = []
        
        def recurse(node,arr):
            nonlocal output
            if not node:
                return 
            
            
            if not node.left and not node.right:
                arr.append(node.val)
                string = "->".join(list(map(str,arr)))
                output.append(string)
                # return
                
            
             
           
            recurse(node.left,arr + [node.val])
            recurse(node.right,arr + [node.val])
            
        
        recurse(root,[])
        
        return output
        
        
        
        
        
        
        
