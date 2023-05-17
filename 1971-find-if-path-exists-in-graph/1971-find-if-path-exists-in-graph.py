class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parents = [i for i in range(n)]
        
        
        def representative(x):
            if parents[x] == x:
                return x
            
            return representative(parents[x])
        
        def union(x,y):
            parx = representative(x)
            pary = representative(y)
            
            if parx != pary:
                parents[pary] = parx
                
                
        for a,b in edges:
            union(a,b)
            
        
        return representative(source) == representative(destination)
        
        
        