class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        count_x = 0
        count_o = 0
        
        for i in range(3):
            for j in range(3):
                if board[i][j] == "X":
                    count_x += 1
                
                if board[i][j] == "O":
                    count_o += 1
                    
        if count_x == count_o or count_x -1 == count_o:
            if (count_x + count_o) % 2 == 0:
                if board[0][0]+board[1][0]+board[2][0] == "XXX" or board[0][1]+board[1][1]+board[2][1] == "XXX" or board[0][2]+board[1][2]+board[2][2] == "XXX" or board[0][0]+board[0][1]+board[0][2] == "XXX" or board[1][0]+board[1][1]+board[1][2] == "XXX" or board[2][0]+board[2][1]+board[2][2] == "XXX" or board[0][0]+board[1][1]+board[2][2]=="XXX" or board[0][2]+board[1][1]+board[2][0]=="XXX":
                        return False
                else:
                    return True
            if (count_x + count_o)%2 != 0:
                    if board[0][0]+board[1][0]+board[2][0] == "OOO" or board[0][1]+board[1][1]+board[2][1] == "OOO" or board[0][2]+board[1][2]+board[2][2] =="OOO" or board[0][0]+board[0][1]+board[0][2] == "OOO" or board[1][0]+board[1][1]+board[1][2] == "OOO" or board[2][0]+board[2][1]+board[2][2] == "OOO" or board[0][0]+board[1][1]+board[2][2]=="OOO" or board[0][2]+board[1][1]+board[2][0]=="OOO":
                        return False
                    else:
                        return True
        else:
            return False
        