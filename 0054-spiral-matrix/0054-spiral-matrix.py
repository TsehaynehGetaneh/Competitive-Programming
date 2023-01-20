class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        direction = "right"
        
        right = 0
        down = len(matrix[0])-1
        left = len(matrix)-1
        up = 0
        
        while right <= left and up <= down:
            # move right
            if direction == "right":
                for j in range(up,down+1):
                    output.append(matrix[right][j])
                
                direction = "down"
                right += 1
                
                if right > left:
                    break
            
            # move down
            if direction == "down":
                for j in range(right,left+1):
                    # print(matrix[j][down])
                    output.append(matrix[j][down])
                    
                direction = "left"
                down -= 1
                
                if down < up:
                    break
                
            if direction == "left":
                for j in range(down,up-1,-1):
                    # print(matrix[left][j])
                    output.append(matrix[left][j])
                    
                direction = "up"
                left -= 1
                
                if left < right:
                    break
                
            if direction == "up":
                for j in range(left,right-1,-1):
                    print(matrix[j][up])
                    output.append(matrix[j][up])
                    
                direction = "right"
                up += 1
                
                if up > down:
                    break
                
                
        
        return output