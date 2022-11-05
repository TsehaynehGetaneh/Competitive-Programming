class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in "+-*/":
                stack.append(int(tokens[i]))
            else:
                if tokens[i] == "+":
                    if len(stack) >=2:
                        add = stack[-2] + stack[-1]
                        stack.pop()
                        stack.pop()
                        stack.append(add)
                if tokens[i] == "-":
                    if len(stack) >=2:
                        subtract = stack[-2] - stack[-1]
                        stack.pop()
                        stack.pop()
                        stack.append(subtract)
                if tokens[i] == "*":
                    if len(stack) >=2:
                        multiply = stack[-2] * stack[-1]
                        stack.pop()
                        stack.pop()
                        stack.append(multiply)
                if tokens[i] == "/":
                    if len(stack) >=2:
                        divide = int(stack[-2] / stack[-1])
                        stack.pop()
                        stack.pop()
                        stack.append(divide)
        return stack[0]