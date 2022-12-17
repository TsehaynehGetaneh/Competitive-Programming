class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        numOfRow = len(grid)
        numOfCol = len(grid[0])
        maxSum = 0
        for i in range(numOfRow -2):
            for j in range(numOfCol -2):
                currSum = sum(grid[i][j:j+3]) + grid[i+1][j+1] + sum(grid[i+2][j:j+3])
                if maxSum < currSum:
                    maxSum = currSum
                    currSum = 0
                else:
                    currSum = 0
        return maxSum