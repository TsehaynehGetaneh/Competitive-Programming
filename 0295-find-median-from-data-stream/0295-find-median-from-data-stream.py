class MedianFinder:

    def __init__(self):
        self.max_values = []
        self.min_values = []
        heapq.heapify(self.max_values)
        heapq.heapify(self.min_values)
    
    def addNum(self, num: int) -> None:
        if len(self.min_values) == len(self.max_values):
            num = - num
            heapq.heappush(self.min_values,num)
            
            if self.max_values:
                min_val = self.max_values[0]
                max_val = -self.min_values[0]
                
                if max_val > min_val:
                    heapq.heappop(self.min_values)
                    heapq.heappop(self.max_values)
                    heapq.heappush(self.min_values,-min_val)
                    heapq.heappush(self.max_values,max_val)
        else:
            heapq.heappush(self.max_values,num)
            
            if self.min_values:
                min_val = self.max_values[0]
                max_val = - self.min_values[0]
                
                if max_val > min_val:
                    heapq.heappop(self.max_values)
                    heapq.heappop(self.min_values)
                    heapq.heappush(self.min_values,-min_val)
                    heapq.heappush(self.max_values,max_val)
                 
    def findMedian(self) -> float:
      
        if self.min_values and self.max_values:
            
            if (len(self.min_values) + len(self.max_values)) %2 == 0:
               
                return (-self.min_values[0] + self.max_values[0])/2
            else:
                if len(self.max_values) > len(self.min_values):
                    return self.max_values[0]
                else:
                    return -self.min_values[0]
        elif self.min_values:
            return -self.min_values[0]
        elif self.max_values:
            return self.max_values[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()