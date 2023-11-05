class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        
        for a,b in relations:
            graph[a].append(b)
            
        
        max_time = {}
        def dfs(node):
            if node in max_time:
                return max_time[node]
            
            res = time[node-1]
            for neighbour in graph[node]:
                res = max(res,time[node-1]+dfs(neighbour))
               
            max_time[node] = res
                
            return res
        
        for i in range(1,n+1):
            dfs(i)
        print(max_time)        
        return max(max_time.values())
                
        