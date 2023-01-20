class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        output = []
        row = []
        col = []
        
        for i in range(len(grid)):
            count_1 = grid[i].count(1)
            count_0 = grid[i].count(0)
            
            row.append((count_1,count_0))
            
        for i in range(len(grid[0])):
            count_1 = 0
            count_0 = 0
            for j in range(len(grid)):
                val = grid[j][i]
                
                if val == 0:
                    count_0 += 1
                else:
                    count_1 += 1
            
            col.append((count_1,count_0))
            
        print(row,col)
        for i in range(len(grid)):
            r = []
            for j in range(len(grid[0])):
                diff = row[i][0]+col[j][0] - row[i][1] - col[j][1]
                r.append(diff)
            
            output.append(r)
            
        return output
                
                
                    
            
                