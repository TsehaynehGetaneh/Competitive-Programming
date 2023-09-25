class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        sa = []
        for i in range(len(scores)):
            sa.append((ages[i],scores[i]))
            
        sa.sort()
        dp = [sa[i][1] for i in range(len(scores))]
        
        for i in range(len(sa)):
            for j in range(i):
                if sa[j][1] <= sa[i][1]:
                    dp[i] = max(dp[i], dp[j]+sa[i][1])
                   
        return  max(dp)
        
        
        