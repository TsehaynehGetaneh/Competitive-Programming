class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points,key = lambda x : x[1])
        
        prev_ft= points[0][1]
        count = 1
        for i in range(1,len(points)):
            if points[i][0] > prev_ft:
                count += 1
                prev_ft = points[i][1]
            
        return count