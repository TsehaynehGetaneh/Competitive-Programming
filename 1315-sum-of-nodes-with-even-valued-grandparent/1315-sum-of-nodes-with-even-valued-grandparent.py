# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        summ = 0
        
        def dfs(node,path):
            nonlocal summ
            if not node:
                return 
            
            curr_path = path + [node.val]
            n = len(curr_path)
            # print(n,curr_path)
            if len(curr_path) >= 3:
                num = curr_path[n-3]
                if num%2 == 0:
                    print(num)
                    summ += node.val
            
            dfs(node.left,path+[node.val])
            dfs(node.right,path+[node.val])
            
        dfs(root,[])
        
        return summ
        