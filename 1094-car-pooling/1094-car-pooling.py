class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_km = float("-inf")
        for trip in trips:
            if max_km < trip[2]:
                max_km = trip[2]
                
        locations = [0] * (max_km + 1)
        
        for trip in trips:
            no_passengers,start,end = trip
            
            locations[start] += no_passengers
            
            if end < len(locations):
                locations[end] -= no_passengers
        print(locations)
        # compute prefix sum of locations
        for i in range(1,len(locations)):
            locations[i] += locations[i-1]
        print(locations)   
        # check if the capacity of each location
        for location in locations:
            if location > capacity:
                return False
            
        return True
        