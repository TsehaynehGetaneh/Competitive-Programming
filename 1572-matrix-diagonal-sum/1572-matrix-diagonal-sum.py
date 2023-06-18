class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        primary_sum = 0
        visited = set()
        col = 0
        for i in range(len(mat)):
            primary_sum += mat[i][col]
            visited.add((i,col))
            col += 1
            
        secondary_sum = 0
        col = len(mat[0]) - 1
        for i in range(len(mat)):
            if (i,col) not in visited:
                secondary_sum += mat[i][col]
            col -= 1
            
        return primary_sum + secondary_sum 
            
        