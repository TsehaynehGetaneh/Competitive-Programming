class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n+1)
        
        for i in range(n-1,-1,-1):
            point,idx = questions[i]
            nxt_idx = i+idx+1
            
            nxt_idx = n if nxt_idx > n else nxt_idx
            
            dp[i] = max(dp[i+1],point + dp[nxt_idx])
           
        return dp[0]
        
                
        