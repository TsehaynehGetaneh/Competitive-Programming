class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        if r*c == len(mat) * len(mat[0]):
            reshape_matrix = []
            
            row = []
            count = 0
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    row.append(mat[i][j])
                    count += 1
                    
                    if count == c:
                        reshape_matrix.append(row)
                        row = []
                        count = 0
                        
            return reshape_matrix
                                         
        else:
            return mat
        