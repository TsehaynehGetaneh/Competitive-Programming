# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = self.helper(root,0,1,defaultdict(list))
        
        ans = 0
        for arr in result.values():
            ans = max(ans,max(arr)-min(arr)+1)
            
        return ans
    
    def helper(self,node,row,col,dictionary):
        if not node:
            return
        
        
        dictionary[row].append(col)
        
        
        self.helper(node.left,row+1,2*col,dictionary)
        self.helper(node.right,row+1,2*col+1,dictionary)
        
        
        return dictionary