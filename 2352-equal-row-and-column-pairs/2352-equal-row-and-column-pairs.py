class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols = []
        
        for i in range(len(grid)):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            
            cols.append(col)
         
        count = 0
        for i in range(len(grid)):
            for j in range(len(cols)):
                if grid[i] == cols[j]:
                    count += 1
                
                
        return count