class Solution:
    def countOrders(self, n: int) -> int:
        slots = 2*n
        count = 1
        while slots > 0:
            count *= slots*(slots-1)//2
            
            slots -= 2
            
        return count%(10**9 + 7)
            
        