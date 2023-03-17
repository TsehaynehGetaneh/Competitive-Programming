class Solution:
    def decodeString(self, s: str) -> str:
        # using stack
        stack = []
        
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                sub_str = ""
                while stack and stack[-1] != "[":
                    sub_str = stack.pop() + sub_str
                    
                stack.pop()
                
                digits = ""
                while stack and stack[-1].isdigit():
                    digits = stack.pop() + digits
                    
                stack.append(sub_str*int(digits))
                
        return "".join(stack)