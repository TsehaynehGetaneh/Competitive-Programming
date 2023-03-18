class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        result = self.kthGrammar(n-1,k//2 + k%2)
        
        is_k_odd = k%2 == 1
        
        if result == 1:
            return 1 if is_k_odd else 0
        
        else:
            return 0 if is_k_odd else 1
        