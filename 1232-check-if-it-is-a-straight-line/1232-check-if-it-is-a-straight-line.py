class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        
        y = (coordinates[1][1] - coordinates[0][1])
        x = (coordinates[1][0] - coordinates[0][0])
        slope = None
        
        if x != 0:
            slope = y/x
        
        for i in range(2, len(coordinates)):
            change_in_y = (coordinates[i][1] - coordinates[i-1][1])
            change_in_x = (coordinates[i][0] - coordinates[i-1][0])
            
            if slope == None:
                if change_in_x != 0:
                    return False
                
            else:
                if change_in_x == 0:
                    return False
                else:
                    if slope != (change_in_y)/ (change_in_x):
                        return False
            
        return True