class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_ends = []
        for i in range(len(matrix)):
            row_ends.append(matrix[i][-1])
        
        idx = -1
        for i in range(len(row_ends)):
            if row_ends[i] >= target:
                idx = i
                break
                
        if idx != -1:
            row = matrix[idx]
            
            for i in range(len(row)):
                if target in row:
                    return True
                else:
                    return False
        else:
            return False