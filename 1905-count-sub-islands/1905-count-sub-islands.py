class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        is_true = True
        count = 0
        
        def dfs(row,col):
            nonlocal visited,is_true
            for a,b in directions:
                r,c = row+a, col+b
                if (0<=r<len(grid2)) and (0<=c<len(grid2[0])) and grid2[r][c] == 1 and (r,c) not in visited:
                    visited.add((r,c))
                    if grid1[r][c] != 1:
                        is_true = False
                    dfs(r,c)
            
        
        
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                
                if grid2[i][j] == 1 and (i,j) not in visited and grid1[i][j] == 1:
                    visited.add((i,j))
                    dfs(i,j)
                    if is_true:
                        count += 1
                    else:
                        is_true = True
        
        return count
                        
                        
                        
            
        