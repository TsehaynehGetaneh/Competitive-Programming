class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        len_col = len(matrix[0])
        zero_rows = set()
        zero_cols = set()
        
        for i in range(len(matrix)):
            for j in range(len_col):
                
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
                    
        for i in range(len(matrix)):
            for j in range(len_col):
                
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0
        
        