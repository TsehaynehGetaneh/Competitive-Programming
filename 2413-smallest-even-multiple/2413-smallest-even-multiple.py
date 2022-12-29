class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        multiply = 1
        
        while n >=1:
            if n%2 == 0:
                return n
            
            n *= multiply
            multiply += 1
        