class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.split("+")
        n1,m1 = int(num1[0]),int(num1[1][:-1])
        
        num2 = num2.split("+")
        n2,m2 = int(num2[0]),int(num2[1][:-1])
        
        result = str(n1*n2 + (m1*m2)*-1) + "+" + str(n1*m2 + m1*n2) + "i"
        
        return result

        
        
                
        