class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        totalSum = 0
        
        for op in operations:
            if op == "C":
                scores.pop()
            elif op == "D":
                scores.append(scores[-1]*2)
            elif op == "+":
                scores.append(scores[-2] + scores[-1])
            else:
                scores.append(int(op))
                
        return sum(scores)