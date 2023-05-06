# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # BFS
        
        
        
        
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj_list = defaultdict(list)
        def dfs(node):
            if not node:
                return
            
            if node.left and node.right:
                a,b,c = node.val,node.left.val,node.right.val
                adj_list[a].append(b)
                adj_list[a].append(c)
                adj_list[b].append(a)
                adj_list[c].append(a)
                
                dfs(node.left)
                dfs(node.right)
                
            elif node.left:
                a,b = node.val,node.left.val
                adj_list[a].append(b)
                adj_list[b].append(a)
                
                dfs(node.left)
            
            elif node.right:
                a,b = node.val,node.right.val
                adj_list[a].append(b)
                adj_list[b].append(a)
                
                dfs(node.right)
                
        dfs(root)
        
        if k == 0:
            return [target.val]
        
        # BFS
        queue = deque()
        queue.append((0,target.val))
        visited = set()
        visited.add(target.val)
        res = []
        while queue:
            level,val = queue.popleft()
            
            for child in adj_list[val]:
                if child not in visited:
                    queue.append((level+1,child))
                    visited.add(child)
                    
                    if level+1 == k:
                        res.append(child)
                        
                        
        return res
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        