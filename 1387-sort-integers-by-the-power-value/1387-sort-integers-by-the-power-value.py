class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}
        def dp(num,steps):
            if num == 1:
                return steps
            
            if num in memo:
                return steps + memo[num]
            
            if num%2 == 0:
                return dp(num//2,steps+1)
                
            if num%2 != 0:
                return dp(num*3+1,steps+1)
                
            
        
        res = []
        for i in range(lo,hi+1):
            count = dp(i,0)
            res.append((count,i))
            memo[i] = count
            
        res.sort()
        print(memo)
        return res[k-1][1]