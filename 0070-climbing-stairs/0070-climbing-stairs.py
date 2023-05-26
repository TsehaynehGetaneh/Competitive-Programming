class Solution:
    def memo(self,n,catch):
        if n <= 2:
            return n
        
        if n in catch:
            return catch[n]
        
        catch[n] = self.memo(n-1,catch) + self.memo(n-2,catch)
        
        return catch[n]
    def climbStairs(self, n: int) -> int:
        
        return self.memo(n,{})
        