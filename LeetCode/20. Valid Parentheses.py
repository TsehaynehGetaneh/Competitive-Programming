class Solution:
    def isValid(self, s: str) -> bool:
        isValid = True
        stack = []
        if len(s) == 1:
            isValid = False
        else:
            for i in range(len(s)):
                if s[i] == "(" or s[i] == "{" or s[i] == "[":
                    stack.append(s[i])
                if s[i] == ")" or s[i] == "}" or s[i] == "]":
                    if s[i] == ")":
                        if len(stack) !=0 and stack[-1] == "(":
                            stack.pop()
                        else:
                            isValid = False
                            break
                    if s[i] == "]":
                        if len(stack) !=0 and stack[-1] == "[":
                            stack.pop()
                        else:
                            isValid = False
                            break
                    if s[i] == "}" and len(stack) !=0:
                        if len(stack) !=0 and stack[-1] == "{":
                            stack.pop()
                        else:
                            isValid = False
                            break
                            
        return isValid and len(stack) == 0