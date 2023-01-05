class Solution:
    def judgeCircle(self, moves: str) -> bool:
        countLeftMoves = 0
        countRightMoves = 0
        countUpMoves = 0
        countDownMoves = 0
        
        for direction in moves:
            if direction == "L":
                countLeftMoves += 1
            elif direction == "R":
                countRightMoves += 1
            elif direction == "U":
                countUpMoves += 1
            elif direction == "D":
                countDownMoves += 1
            
        if countLeftMoves == countRightMoves and countUpMoves == countDownMoves:
            return True
        else:
            return False
            
        