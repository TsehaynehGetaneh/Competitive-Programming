class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(bombs)):
            x,y,r = bombs[i]
            for j in range(len(bombs)):
                if j != i:
                    x2,y2,r2 = bombs[j]
                    
                    if (abs(x2-x)**2 + abs(y2-y)**2) <= r**2:
                        graph[i].append(j)
         
        def dfs(vertex,visited):
            nonlocal count 
            visited.add(vertex)
            
            for child in graph[vertex]:
                if child not in visited:
                    count += 1
                    dfs(child,visited)
           
                    
            return count
        
        
        max_ = 1
        for i in range(len(bombs)):
            count = 1
            dfs(i,set())
            
            max_ = max(max_,count)
            
        return max_