# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        ans = defaultdict(list)
        
        def dfs(node,idx):
            nonlocal ans
            if not node:
                return 
            
            ans[idx].append(node.val)
            
            dfs(node.left,idx+1)
            dfs(node.right,idx+1)
            
            
            
        dfs(root,0)
        
        res = []
        for key,val in ans.items():
            res.append(val)
        
        return sum(res[-1])
        