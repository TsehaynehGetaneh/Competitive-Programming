class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        root = [i for i in range(n)]
        rank = [1 for i in range(n)]
        
        def find(x):
            if x == root[x]:
                return x
            
            if x != root[x]:
                root[x] = find(root[x])
                
            return root[x]
        
        def union(x,y):
            nonlocal rank
            rootX = find(x)
            rootY = find(y)
            
            if rootX != rootY:
                if rank[rootX] < rank[rootY]:
                    root[rootX] = rootY
                elif rank[rootX] > rank[rootY]:
                    root[rootY] = rootX
                    
                else:
                    root[rootY] = rootX
                    rank[rootX] += 1
                
        for a,b in edges:
            union(a,b)
            
        return find(source) == find(destination)
            
        
            
        
        
        