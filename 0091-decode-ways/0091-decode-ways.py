class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {len(s): 1}
        
        def dp(idx):
            if idx in cache:
                return cache[idx]
            
            if s[idx] == "0":
                return 0
            
            res = dp(idx+1)
            print(idx,res,cache)
            if (idx+1 < len(s) and (s[idx] == "1" or s[idx] == "2" and s[idx+1] in "0123456")):
                res += dp(idx+2)
                
            cache[idx] = res
            print("after",res,cache)  
            return res
        
        return dp(0)
                
        