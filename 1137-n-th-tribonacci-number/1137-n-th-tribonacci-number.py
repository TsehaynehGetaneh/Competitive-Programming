class Solution:
    def memo(self,n,catch):
        if n <= 1:
            return n
        
        if n == 2:
            return 1
        
        if n in catch:
            return catch[n]
        
        catch[n] = self.memo(n-1,catch) + self.memo(n-2,catch) + self.memo(n-3,catch)
        
        return catch[n]
    
    def tribonacci(self, n: int) -> int:
        return self.memo(n,{})