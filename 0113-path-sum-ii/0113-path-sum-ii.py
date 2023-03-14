# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        
        def dfs(node,arr):
            nonlocal ans
            if not node:
                return
            
            if not node.left and not node.right:
                arr.append(node.val)
                if sum(arr) == targetSum:
                    ans.append(arr)
                    
                    
            dfs(node.left,arr+[node.val])
            dfs(node.right,arr+[node.val])
            
            
        dfs(root,[])
        
        return ans