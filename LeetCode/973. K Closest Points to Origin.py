class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k >=  1:
            points.sort(key = lambda point:point[0]**2 + point[1]**2)
                    
        return points[0: k]