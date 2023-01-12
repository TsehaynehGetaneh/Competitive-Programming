class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        col_len = len(strs[0])
        
        for i in range(col_len):
            isInc = True

            for j in range(1,len(strs)):
                if strs[j-1][i] > strs[j][i]:
                    isInc = False
                   
            if isInc == False:
                count += 1
                
        return count
            
            