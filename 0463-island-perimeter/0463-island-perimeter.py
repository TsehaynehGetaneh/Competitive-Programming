class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    
                    # check left
                    if j-1 >= 0 and grid[i][j-1] == 1:
                        count += 1
                        
                    # check right
                    if j+1 < len(grid[0]) and grid[i][j+1] == 1:
                        count += 1
                        
                    # check top
                    if i-1 >= 0 and grid[i-1][j] == 1:
                        count += 1
                        
                    # check bottom
                    if i+1 < len(grid) and grid[i+1][j] == 1:
                        count += 1
                else:
                    # check left
                    if j-1<0:
                        count += 1
                    # check right
                    if j+1 >= len(grid[0]):
                        count += 1
                    #check top
                    if i-1 <0:
                        count += 1
                    # check bottom
                    if i+1 >= len(grid):
                        count += 1
                    print(count)    
        return count
        