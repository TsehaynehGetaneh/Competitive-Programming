class Solution:
        
    def findTheDifference(self, s: str, t: str) -> str:
        dic_s = {}
        dic_t = {}
        for i in s:
            if i in dic_s:
                dic_s[i] += 1
            else:
                dic_s[i] = 1
        for i in t:
            if i in dic_t:
                dic_t[i] += 1
            else:
                dic_t[i] = 1
                
        if len(s) == 0 and len(t) == 1:
            return t[0]
        
        for i in t:
            if i not in s or dic_t[i] > dic_s[i]:
                return i
            
            
        
        