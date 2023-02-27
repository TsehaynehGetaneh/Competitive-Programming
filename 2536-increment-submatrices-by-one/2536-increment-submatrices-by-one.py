class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        res = [[0]*n for i in range(n)]
        
        
        for query in queries:
            row1,col1,row2,col2 = query
            
            for i in range(row1,row2+1):
                res[i][col1] += 1
                
                if col2 + 1 < len(res[0]):
                    res[i][col2+1] -= 1
                      
        for i in range(len(res)):
            for j in range(1,len(res[0])):
                res[i][j] += res[i][j-1]
                
                
        return res
                
            
            
        