class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        new_grid = []
        for arr in grid:
            arr = sorted(arr)
            new_grid.append(arr)
            
       
        ans = 0
        for i in range(len(new_grid[0])):
            max_num = 0
            for j in range(len(new_grid)):
                num = new_grid[j][i]
                max_num = max(max_num,num)
               
            ans += max_num
            
            
        return ans        