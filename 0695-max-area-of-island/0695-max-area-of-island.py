class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        
        def dfs(row,col,matrix):
            nonlocal count,rows,cols,visited
            # base case 1
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            
            # base case 2
            if (row,col) in visited or grid[row][col] == 0:
                return
            
            count += 1
            visited.add((row,col))
            
            # move 4-directionally
            dfs(row,col-1,matrix)
            dfs(row,col+1,matrix)
            dfs(row-1,col,matrix)
            dfs(row+1,col,matrix)
            
        
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                
                if (i,j) not in visited and grid[i][j] == 1:
                    count = 0
                    dfs(i,j,grid)
                    max_area = max(max_area,count)
                    
                    
                    
        return max_area
                
                
                
                
                
                
                
                
                
                
                
                
                
            
        