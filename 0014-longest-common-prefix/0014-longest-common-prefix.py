class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        minLen = len(strs[0])
        for string in strs:
            length = len(string)
            minLen = min(length,minLen)
        
        str1 = strs[0]
        lcp = ''
        i = 0
        j = 0
        while i<=j and j<minLen:
            isCommon = True
            cp = ''
            
            for k in range(1,len(strs)):
                if str1[i:j+1] not in strs[k][i:j+1]:
                    isCommon = False
                    
            if isCommon == True:
                cp += str1[i:j+1]
                j += 1
                if len(lcp) < len(cp):
                    lcp = cp
            else:
                break
                    
        return lcp
                
                
        
        
            