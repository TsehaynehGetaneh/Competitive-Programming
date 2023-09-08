class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        source = image[sr][sc]
        
        def backtrack(row,col):
            
            # change color
            if image[row][col] == source:
                image[row][col] = color
            
            
            for a,b in directions:
                if 0<=(row+a)<n and 0<=(col+b)<m and image[row+a][col+b] == source and image[row+a][col+b] != color:
                    backtrack(row+a,col+b)
                
            return image
        
        return backtrack(sr,sc)
                
        