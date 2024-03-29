class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = defaultdict(int)
        
        def dp(row,col):
            
            if row <0 or row>=m or col < 0 or col >= n:
                return 0
            
            if row == m-1 and col == n-1:
                return 1
            
            if (row,col) in memo:
                return memo[(row,col)]
            
            memo[(row,col)] = dp(row+1,col) + dp(row,col+1)
            
            return memo[(row,col)]
                        
        return dp(0,0)
        
        
            
            
            
            
        