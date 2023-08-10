class Solution:
    def close_distance(self,heaters,house):
        left,right = 0, len(heaters)-1
        min_d = float("inf")
        while left <=right:
            mid = (left+right)//2
            min_d = min(min_d,abs(heaters[mid]-house))
            if heaters[mid] < house:
                left = mid + 1
            else:
                right = mid - 1
                
        return min_d
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        radius = 0
        for house in houses:
            radius = max(radius,self.close_distance(heaters,house))
            
        return radius
        