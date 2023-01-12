class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        idx = -1
        for i in range(len(matrix)):
            end = matrix[i][-1]
            
            if target <= end:
                idx = i
                break
        
                
        if idx != -1:
            row = set(matrix[idx])
            
            if target in row:
                return True
            else:
                return False
                
        else:
            return False