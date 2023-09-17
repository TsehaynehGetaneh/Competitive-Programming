class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        original = [pref[0]]
        num = pref[0]
        
        for i in range(1,len(pref)):
            original.append(num ^ pref[i])
            
            num ^= original[-1]
            
        return original
        
        
        