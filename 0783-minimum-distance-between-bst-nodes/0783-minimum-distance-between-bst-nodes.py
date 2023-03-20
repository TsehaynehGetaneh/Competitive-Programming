# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(node,dic):
            if not node:
                return
            dic[0].append(node.val)
            
            dfs(node.left,dic)
            dfs(node.right,dic)
            
            
            return sorted(dic[0])
        
        result = dfs(root,defaultdict(list))
        
        # find the minimum difference
        min_diff = float("inf")
        for i in range(1,len(result)):
            min_diff = min(min_diff,result[i] - result[i-1])
            
        return min_diff
        