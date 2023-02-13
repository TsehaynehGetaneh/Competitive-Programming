class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = 0
        if low%2 != 0 and high%2 != 0:
            return (high-low - 1) // 2 + 2
        elif low%2 != 0 and high%2 == 0:
            return (high-low-1)//2 + 1
        elif low%2 == 0 and high%2 == 0:
            return (high-low-1)//2 + 1
        else:
            return (high-low-1)//2 + 1
            
        