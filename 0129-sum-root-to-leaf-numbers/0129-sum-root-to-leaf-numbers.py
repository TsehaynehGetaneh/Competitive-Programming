# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        sum_ = 0
        def dfs(node,arr):
            nonlocal sum_
            if not node:
                return 
            
            if not node.left and not node.right:
                arr.append(str(node.val))
                num = int("".join(arr))
                sum_ += num
                
                
            dfs(node.left,arr + [str(node.val)])
            dfs(node.right,arr + [str(node.val)])
            
        
        dfs(root,[])
        
        return sum_
        