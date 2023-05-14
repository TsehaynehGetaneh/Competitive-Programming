class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        shortest_path = float("inf")
        queue = deque([(0,(entrance[0],entrance[1]))])
        visited = set()
        visited.add((entrance[0],entrance[1]))
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        
        while queue:
            level,pos = queue.popleft()
            
            for x,y in directions:
                x_,y_ = pos[0] + x, pos[1] + y
            
                if 0<=x_<len(maze) and 0<=y_<len(maze[0]) and maze[x_][y_] == "." and (x_,y_) not in visited:
                    queue.append((level+1,(x_,y_)))
                    visited.add((x_,y_))
                    
                    if y_ == 0 or y_ == len(maze[0])-1 or x_ == 0 or x_ == len(maze)-1:
                        shortest_path = min(shortest_path,level+1)
                        
        return shortest_path if shortest_path != float("inf") else -1
        