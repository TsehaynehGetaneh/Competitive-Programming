class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        smallestD = float("inf")
        idx = -1
        
        for i in range(len(points)):
            
            if points[i][0] == x or points[i][1] == y:
                distance = abs(points[i][0]-x) + abs(points[i][1]-y)
                
                if distance < smallestD:
                    smallestD = distance
                    idx = i
        
        return idx
            
        