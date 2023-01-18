class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_arr = []
            col_arr = []
            
            for j in range(9):
                if board[i][j] != ".":
                    if int(board[i][j])<1 or int(board[i][j])>9:
                        return False

                    row_arr.append(int(board[i][j]))

                if board[j][i] != ".":
                    if int(board[j][i])<1 or int(board[j][i])>9:
                        return False

                    col_arr.append(int(board[j][i]))
            
            if len(col_arr) != len(set(col_arr)):
                return False
            
            if len(row_arr) != len(set(row_arr)):
                return False
          
        
        # check each 3*3 matrix
        
        for i in range(0,7,3):
            for j in range(0,7,3):
                
                val1,val2,val3 = board[i][j],board[i+1][j],board[i+2][j]
                val4,val5,val6 = board[i][j+1],board[i+1][j+1],board[i+2][j+1]
                val7,val8,val9 = board[i][j+2],board[i+1][j+2],board[i+2][j+2]
                
                arr = [val1,val2,val3,val4,val5,val6,val7,val8,val9]
                new_arr = []
                for val in arr:
                    if val != ".":
                        num = int(val)
                        new_arr.append(num)
                        
                        if num<1 or num>9:
                            return False
                if len(new_arr) != len(set(new_arr)):
                    return False
                    
                        
                
        return True
            
            
                