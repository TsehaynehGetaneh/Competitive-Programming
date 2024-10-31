class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for punc in s:
            if not stack:
                stack.append(punc)
            elif punc not in ")}]":
                stack.append(punc)

            else:
                if (punc == ")" and stack[-1] == "(") or \
                punc == "}" and stack[-1] == "{" or \
                punc == "]" and stack[-1] == "[":
                    stack.pop()

                else:
                    stack.append(punc)

        return len(stack) == 0
        