class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ = 0
        product = 1
        
        while n > 0: 
            rem = n%10
            
            summ += rem
            product *= rem
            
            n //= 10
            
        return product - summ