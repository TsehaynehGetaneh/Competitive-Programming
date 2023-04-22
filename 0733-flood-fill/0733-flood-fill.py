class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        rows,cols = len(image),len(image[0])
        def dfs(i,j,matrix):
            # Base case 1
            if i<0 or i>=rows or j<0 or j>=cols:
                return 
            
            # base case 2
            if start_color != matrix[i][j] or matrix[i][j]==color:
                return
            
            matrix[i][j] = color
            
            # move 4-directionally
            dfs(i-1,j,matrix) 
            dfs(i,j-1,matrix) 
            dfs(i+1,j,matrix) 
            dfs(i,j+1,matrix) 
        
        dfs(sr,sc,image)
        return image