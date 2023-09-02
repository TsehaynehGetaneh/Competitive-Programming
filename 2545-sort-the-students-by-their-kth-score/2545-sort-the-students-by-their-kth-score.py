class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        n = len(score)
        kth_column = []
        
        for i in range(n):
            kth_column.append((score[i][k],i))
            
        kth_column = sorted(kth_column,reverse = True)
        
        # final array
        ans = []
        for i in range(n):
            idx = kth_column[i][1]
            ans.append(score[idx])
            
        return ans