class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dic = {}
        
        def dp(row,col):
            
            if (row >= len(triangle)) or (col >= len(triangle[row])):
                return 0
            
            if (row,col) in dic:
                return dic[(row,col)]
            
            left = dp(row+1,col)
            right = dp(row+1,col+1)
            
            dic[(row,col)] = triangle[row][col] + min(left,right)
            
            
            return dic[(row,col)]
        
        return dp(0,0)
        
        
        
        
       
        