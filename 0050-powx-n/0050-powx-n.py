class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recursive(x,n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            ans = recursive(x,n//2)
            ans = ans * ans
            
            return x*ans if n%2 != 0 else ans 
            
        res = recursive(x,abs(n))
        
        
        return res if n >= 0 else 1/res
        