class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        
        if (len(grid)>=3 and len(grid[0])>=3):
            
            for i in range(len(grid)-2):
                for j in range(len(grid[0])-2):
                    values = []
                    val1,val2,val3 = grid[i][j],grid[i][j+1],grid[i][j+2]
                    val4,val5,val6 = grid[i+1][j],grid[i+1][j+1],grid[i+1][j+2]
                    val7,val8,val9 = grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2]
                    
                    values.extend([val1,val2,val3,val4,val5,val6,val7,val8,val9])
                    idx = 0
                    while idx<len(values):
                        if values[idx] > 9 or values[idx] < 1:
                            values.remove(values[idx])
                        else:
                            idx += 1
                            
                    values = set(values)
                    print(values)
                    if len(values) == 9:
                        row1,row2 = val1 + val2 + val3,val4 + val5 + val6
                        row3 = val7 + val8 + val9

                        col1,col2 = val1 + val4 + val7,val2 + val5 + val8
                        col3 = val3 + val6 + val9

                        d1,d2 = val1 + val5 + val9,val3 + val5 + val7
                        
                        max_sum = max(row1,row2,row3,col1,col2,col3,d1,d2)
                        min_sum = min(row1,row2,row3,col1,col2,col3,d1,d2)
                        print(min_sum,max_sum)
                        if min_sum == max_sum:
                            count += 1
                    
                    
        return count



        