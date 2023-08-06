class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo = {}
        def dp(row,col):
            if row >= len(matrix):
                return 0
            
            if col < 0 or col >= len(matrix[0]):
                return 10000
            
            if (row,col) in memo:
                return memo[(row,col)]
           
            memo[(row,col)] = matrix[row][col] + min(dp(row+1,col),dp(row+1,col-1),dp(row+1,col+1))
            
            return memo[(row,col)]
        
        
        min_sum = inf
        for i in range(len(matrix[0])):
            sub_sum = dp(0,i)
            min_sum = min(min_sum,sub_sum)
          
        return min_sum
        
        
        


                
        
        