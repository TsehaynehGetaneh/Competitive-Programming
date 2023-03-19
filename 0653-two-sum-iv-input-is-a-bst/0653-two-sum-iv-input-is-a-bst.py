# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return self.helper(root,k,defaultdict())
    
    
    def helper(self,node,k,dic):
        if not node:
            return False 
        
        if k - node.val in dic:
            return True
        
        dic[node.val] = node.val
        # print(dic)
        
        return self.helper(node.left,k,dic) or self.helper(node.right,k,dic)
        
        
    
        