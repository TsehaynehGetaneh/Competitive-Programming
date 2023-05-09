class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        min_heap = [-n for n in piles]
        heapq.heapify(min_heap)

        for i in range(k):
            max_val = -heapq.heappop(min_heap)
            heapq.heappush(min_heap,-(max_val - max_val//2))
            
        return -sum(min_heap)