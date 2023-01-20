class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        output = []
        reverse = True
        
        for i in range(len(mat)):
            if i == 0:
                for j in range(len(mat[0])):
                    row = []
                    val = mat[i][j]
                    row.append(val)
                    r,c = i,j
                    while r+1 < len(mat) and c-1 >= 0:
                        r += 1
                        c -=1
                        row.append(mat[r][c])
                    print(row)
                    if reverse == True and len(row)>0:
                        row.reverse()
                        output.extend(row)
                        reverse = False
                    else:
                        output.extend(row)
                        reverse = True
            else:
                row = []
                j = len(mat[0])-1
                val = mat[i][j]
                row.append(val)
                r,c = i,j
                while r+1 < len(mat) and c-1 >= 0:
                    r += 1
                    c -=1
                    row.append(mat[r][c])
                    
                    
                if reverse == True and len(row)>0:
                    row.reverse()
                    output.extend(row)
                    reverse = False
                else:
                    output.extend(row)
                    reverse = True
                    
                    
                    
        return output
                
                
        