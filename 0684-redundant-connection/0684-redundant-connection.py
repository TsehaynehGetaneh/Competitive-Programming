class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges))]
        rank = [1]*len(edges)
        
        def representative(node):
            if parents[node] == node:
                return node
            
            parents[node] = representative(parents[node])
            
            return parents[node]
        
        def union(node1,node2):
            par_node1 = representative(node1)
            par_node2 = representative(node2)
            
            if par_node1 != par_node2:
                if rank[par_node1] < rank[par_node2]:
                    parents[par_node1] = par_node2
                    
                elif rank[par_node2] < rank[par_node1]:
                    parents[par_node2] = par_node1
                    
                else:
                    parents[par_node2] = par_node1
                    rank[par_node1] += 1
        
        
        ans = []
        for a,b in edges:
            if representative(a-1) != representative(b-1):
                union(a-1,b-1)
            else:
                ans = [a,b]
            
            
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
        