class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        queue = deque([])
        topological_sort = []
        indegree = [0]* numCourses
        adj_list = defaultdict(list)
        
        for course,pre in prerequisites:
            adj_list[pre].append(course)
            indegree[course] += 1
            
            
        # add nodes w/c has indegree zero
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
                
        while queue:
            course = queue.popleft()
            topological_sort.append(course)
            
            for child in adj_list[course]:
                indegree[child] -= 1
                
                if indegree[child] == 0:
                    queue.append(child)
                    
        
        if len(topological_sort) == numCourses:
            return True
        
        return False
    
    
    
    
    
    
        