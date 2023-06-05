class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = len(s) - 1
        
        for j in range(len(t)-1,-1,-1):
            if idx >=0 and t[j] == s[idx]:
                idx -= 1
                
            
            if idx < 0:
                break
                
        return idx < 0
        
        