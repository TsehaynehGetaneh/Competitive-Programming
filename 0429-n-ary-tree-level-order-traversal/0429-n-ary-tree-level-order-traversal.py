"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = defaultdict(list)
        
        def dfs(node,level):
            if not node:
                return
            
            ans[level].append(node.val)
            
            for child in node.children:
                dfs(child,level+1)
                
                
        dfs(root,0)
        
        # result
        res = []
        for key,val in ans.items():
            res.append(val)
            
        return res
        