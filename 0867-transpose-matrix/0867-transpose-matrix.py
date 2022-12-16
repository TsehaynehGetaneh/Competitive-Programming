class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix[0])
        idx = 0
        res = []
        while idx < n:
            arr = []
            for i in range(len(matrix)):
                arr.append(matrix[i][idx])
            res.append(arr)
            idx += 1
        return res
        