class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        counter_p = Counter(p)
        counter = Counter(s[0:len(p)])
        res = []
        
        if counter == counter_p:
            res.append(0)
        
        i = 0
        j = len(p)
        
        while j < len(s):
            counter[s[i]] -= 1
            
            counter[s[j]] += 1
            
            if counter == counter_p:
                res.append(i+1)
                
            i += 1
            j += 1
            
        return res
    
            
            
        