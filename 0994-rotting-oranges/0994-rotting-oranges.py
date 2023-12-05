class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0,-1),(0,1),(-1,0),(1,0)]
        n,m = len(grid), len(grid[0])
        count = 0
        
        queue = deque()
        fresh_oranges = 0
        
        # track fresh and rotten oranges
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1
                    
        # if no fresh oranges
        if fresh_oranges < 1:
            return 0
        
        while queue:
            true = False
            size = len(queue)
            
            for i in range(size):
                row,col = queue.popleft()
            
                for a,b in directions:
                    x,y = row+a, col+b
                    if (x>=0 and x<n) and (y>=0 and y<m) and grid[x][y] == 1:
                        true = True
                        grid[x][y] = 2
                        queue.append((x,y))
                        fresh_oranges -= 1
                    
            if true:
                count += 1
                
        # final result
        if fresh_oranges == 0:
            return count
        else:
            return -1
                
                    
        
                    
                    
                    