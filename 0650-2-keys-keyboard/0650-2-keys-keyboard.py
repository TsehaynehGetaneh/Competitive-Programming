class Solution:
    def minSteps(self, n: int) -> int:
        # It's just the sum of prime factors of n 
        prime_factors = []
        i = 2
        
        while i*i <= n:
            if n%i == 0:
                while n%i == 0:
                    prime_factors.append(i)
                    n //= i
                    
            i += 1
            
        if n > 1:
            prime_factors.append(n)
            
            
        return sum(prime_factors)
        