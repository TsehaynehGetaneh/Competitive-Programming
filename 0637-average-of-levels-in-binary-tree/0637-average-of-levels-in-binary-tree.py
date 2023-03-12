# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = self.helper(root,0,defaultdict(list))
        
        ans = []
        for arr in result.values():
            ans.append(sum(arr)/len(arr))
            
        return ans
        
    def helper(self,node,row,dic):
        if not node:
            return
        
        dic[row].append(node.val)
        
        self.helper(node.left,row+1,dic)
        self.helper(node.right,row+1,dic)
        
        return dic