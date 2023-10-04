class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        
        for a,b in prerequisites:
            graph[a].append(b)
           
        is_true = False   
        def dfs(graph,source,destination,visited):
            nonlocal is_true
            visited.add(source)
            
            for neighbour in graph[source]:
                if destination == neighbour:
                    is_true = True
                if neighbour not in visited:
                    visited.add(neighbour)
                    dfs(graph,neighbour,destination,visited)
                    
            return 
                    
            
            
        
        ans = []
        for src,dest in queries:
            dfs(graph,src,dest,set())
            if is_true:
                ans.append(True)
            else:
                ans.append(False)
                
            is_true = False
            
        return ans
        