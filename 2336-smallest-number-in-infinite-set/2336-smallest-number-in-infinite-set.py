class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.nums = set()
        
        for i in range(1,1001):
            heapq.heappush(self.heap,i)
            self.nums.add(i)
        

    def popSmallest(self) -> int:
        removed_num = heapq.heappop(self.heap)
        self.nums.remove(removed_num)
        return removed_num
        

    def addBack(self, num: int) -> None:
        if num not in self.nums:
            heapq.heappush(self.heap,num)
            self.nums.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)