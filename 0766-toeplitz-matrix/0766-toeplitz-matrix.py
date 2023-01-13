class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        len_col = len(matrix[0])
        isEqual = True
        
        for i in range(1,len(matrix)):
            for j in range(1,len_col):
                if matrix[i-1][j-1] != matrix[i][j]:
                    isEqual = False
                    
        if isEqual == True:
            return True
        else:
            return False
        
            