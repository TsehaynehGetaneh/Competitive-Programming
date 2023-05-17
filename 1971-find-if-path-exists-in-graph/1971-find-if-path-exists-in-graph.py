class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parents = [i for i in range(n)]
        rank = [1] *n
        
        
        def representative(x):
            if parents[x] == x:
                return x
            
            # path compression
            parents[x] = representative(parents[x])
            
            return parents[x]
        
        def union(x,y):
            parx = representative(x)
            pary = representative(y)
            
            if parx != pary:
                if rank[parx] < rank[pary]:
                    parents[parx] = pary
                
                elif rank[parx] > rank[pary]:
                    parents[pary] = parx
                    
                else:
                    parents[pary] = parx
                    rank[parx] += 1
                
                
        for a,b in edges:
            union(a,b)
            
        
        return representative(source) == representative(destination)
        
        
        