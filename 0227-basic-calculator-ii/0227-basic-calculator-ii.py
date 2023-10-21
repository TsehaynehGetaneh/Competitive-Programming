class Solution:
    def calculate(self, s: str) -> int:
        s += " "
        stack = []
        num = 0
        sign = "+"
        
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = num*10 + int(s[i])
                
            elif s[i] in "+-*/" or i == len(s) -1:
                if sign == "+":
                    stack.append(num)
                    
                elif sign == "-":
                    stack.append(-num)
                    
                elif sign == "*":
                    stack.append(stack.pop()*num)
                    
                else:
                    stack.append(int(stack.pop()/num))
                    
                num = 0
                sign = s[i]
                
            i += 1
                                 
        return sum(stack)
        