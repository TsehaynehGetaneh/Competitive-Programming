class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for s,d,w in times:
            graph[s].append((d,w))
           
        distances = {node: float("inf") for node in range(1,n+1)}
        distances[k] = 0
        
        visited = set()
        priority_queue = [(0,k)]
        
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            
            if current_node in visited:
                continue
                
            visited.add(current_node)
            
            for neighbour, weight in graph[current_node]:
                distance = current_distance + weight
                
                if distance < distances[neighbour]:
                    distances[neighbour] = distance
                    
                    heapq.heappush(priority_queue,(distance,neighbour))
                    
                    
        max_distance = 0           
        for node in distances:
            if distances[node] == float("inf"):
                return -1
            max_distance = max(max_distance,distances[node])
            
            
        return max_distance    
            
            
            
            
        