class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        rank = [1]*n
        
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
                    
                elif rank[par_node1] > rank[par_node2]:
                    parents[par_node2] = par_node1
                    
                else:
                    parents[par_node2] = par_node1
                    rank[par_node1] += 1
        
        def connected(x,y):
            return representative(x) == representative(y)
                    
        for a,b,d in roads:
            if parents[a-1] != parents[b-1]:
                union(a-1,b-1)
            
        ans = inf
        for a,b,d in roads:
            if connected(a-1,n-1):
                ans = min(ans,d)
                
        return ans
            
            
            
            
            
            
            
                    
          
        
         
        

                    
        