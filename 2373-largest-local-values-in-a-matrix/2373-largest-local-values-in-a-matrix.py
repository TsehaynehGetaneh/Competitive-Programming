class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        max_values = []
        
        
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                max1 = max(grid[i][j],grid[i][j+1],grid[i][j+2])
                max2 = max(grid[i+1][j],grid[i+1][j+1],grid[i+1][j+2])
                max3 = max(grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2])
                max_val = max(max1,max2,max3)
                
                max_values.append(max_val)
                
        no_cols = len(grid[0]) - 2
        matrix = []
        
        for i in range(0,len(max_values),no_cols):
            matrix.append(max_values[i:i+no_cols])
          
        
        return matrix