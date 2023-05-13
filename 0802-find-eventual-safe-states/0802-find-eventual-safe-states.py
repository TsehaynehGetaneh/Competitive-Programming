class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe_nodes = []
        adj_list = defaultdict(list)
        indegree = [0]*len(graph)
        
        for i in range(len(graph)):
            for node in graph[i]:
                adj_list[node].append(i)
                indegree[i] += 1
                
               
        queue = deque([])
        for i in range(len(indegree)):
            if indegree[i] == 0:
                safe_nodes.append(i)
                queue.append(i)
                
        while queue:
            node = queue.popleft()
            
            for child in adj_list[node]:
                indegree[child] -= 1
                
                if indegree[child] == 0:
                    queue.append(child)
                    safe_nodes.append(child)
            
        return sorted(safe_nodes)
        