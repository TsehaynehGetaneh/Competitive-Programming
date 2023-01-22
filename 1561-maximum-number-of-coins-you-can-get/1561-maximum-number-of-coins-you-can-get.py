class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        total = 0
        
        i = 0
        j = len(piles) -1
        while i < j-1:
            
            total += piles[j-1]
            
            i += 1
            j -= 2
            
        return total
            
        