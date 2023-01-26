class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        total = 0
        
        count = 0
        for i in range(len(piles)-2,-1,-2):
            
            total += piles[i]
            count += 1
            
            if count == len(piles)//3:
                break
            
        return total
            
        