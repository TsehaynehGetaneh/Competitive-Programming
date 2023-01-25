class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = [i**2 for i in range(46340)]
        
        i = 0
        j = len(squares) - 1
        while i<=j:
            if squares[i] + squares[j] == c:
                return True
            
            if squares[i] + squares[j] < c:
                i += 1
            
            if squares[i] + squares[j] > c:
                j -= 1
        
        return False
        