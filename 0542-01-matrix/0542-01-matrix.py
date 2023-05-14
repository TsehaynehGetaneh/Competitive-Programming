class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque([])
        visited = set()
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))
                    
        
        while queue:
            x,y = queue.popleft()
            
            for direction in directions:
                x_,y_ = x+direction[0],y+direction[1]
                
                if 0<=x_<len(mat) and 0<=y_<len(mat[0]) and (x_,y_) not in visited:
                    mat[x_][y_] = mat[x][y] + 1
                    queue.append((x_,y_))
                    visited.add((x_,y_))
                    
        return mat
        