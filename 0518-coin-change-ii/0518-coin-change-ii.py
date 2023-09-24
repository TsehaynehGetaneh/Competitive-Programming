class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        
        def dp(i,total):
            if total == amount:
                return 1
            
            if total > amount or i == len(coins):
                return 0
            
            if (i,total) in cache:
                return cache[(i,total)]
            
            cache[(i,total)] = dp(i,total+coins[i]) + dp(i+1,total)
            
            return cache[(i,total)]
        
        return dp(0,0)