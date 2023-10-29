class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        root = [i for i in range(n)]
        
        def find(x):
            if x == root[x]:
                return x
            
            if x != root[x]:
                root[x] = find(root[x])
                
            return root[x]
        
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            
            if rootX != rootY:
                root[rootX] = rootY
                
        for a,b in edges:
            union(a,b)
            
        return find(source) == find(destination)
            
        
            
        
        
        