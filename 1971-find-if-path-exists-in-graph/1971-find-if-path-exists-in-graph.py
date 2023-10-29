class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True        
        
        graph = defaultdict(list)
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        is_found = False
        
        def dfs(node,visited):
            nonlocal is_found
            
            visited.add(node)
            
            if node == destination:
                is_found = True
                return
            
            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour,visited)
                    
            return is_found
        
        return dfs(source,set())
            
        
        
        