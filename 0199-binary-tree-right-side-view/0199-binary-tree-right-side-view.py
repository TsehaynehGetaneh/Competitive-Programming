# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res  = self.helper(root,0,defaultdict(list))
        
        ans = []
        
        if not res:
            return 
        
        for arr in res.values():
            ans.append(arr[-1])
            
        return ans
       
        
    def helper(self,node,row,mem):
        if not node:
            return 
        
        mem[row].append(node.val)
        
        self.helper(node.left,row+1, mem)
        self.helper(node.right,row + 1, mem)
        
        return mem
       
        