class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = set(list(jewels))
        count = 0
        
        for char in stones:
            if char in j:
                count += 1
                
        return count
        