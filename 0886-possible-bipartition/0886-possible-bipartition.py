class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a,b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        
        # BFS
        visited = set()
        color = [-1] * (n+1)
        queue = deque([])
        for i in range(1,n+1):
            if i in visited:
                continue
              
            visited.add(i)
            queue.append(i)
            color[i] = 0
            
            while queue:
                node = queue.popleft()
                
                for child in graph[node]:
                    
                    if color[child] == -1:
                        color[child] = 1 - color[node]
                        visited.add(child)
                        queue.append(child)
                    
                    elif color[child] == color[node]:
                        return False
                    
        return True
            
        